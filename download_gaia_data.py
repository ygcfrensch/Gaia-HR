import os
import logging
import numpy as np
import pandas as pd
from astroquery.gaia import Gaia
from astropy.table import Table, vstack

logging.getLogger("astroquery").setLevel(logging.ERROR)

# Query Gaia for wanted parameters
def query_gaia(parallax_filter, gaia_source):
	"""
	query_gaia(parallax_filter, gaia_source='gaiadr3.gaia_source')
	parallax_filter: "parallax>=10", "parallax>=5 AND parallax<=10" etc.
	"""
	job_description = f"""SELECT parallax, logg_gspphot, teff_gspphot, phot_g_mean_mag, phot_rp_mean_mag, phot_bp_mean_mag, mh_gspphot, ruwe, parallax_over_error, ag_gspphot, ebpminrp_gspphot
	FROM {gaia_source}
	WHERE {parallax_filter} AND ruwe<1.4 AND parallax_over_error>=10 AND logg_gspphot IS NOT NULL"""
	print(parallax_filter)
    
	job = Gaia.launch_job_async(job_description)
	gtable = job.get_results()
	gtable.remove_columns(["ruwe", "parallax_over_error"])
    
	print('Number of stars in query: %i \n'%(len(gtable['parallax'])))
	return(gtable)
    
# Download necessary HR diagram data
def download_gaia(gaia_source='gaiadr3.gaia_source', max_download_distance=400, delete=False):
	"""
	Download Gaia HR diagram data in volume steps up to max_download_distance, saved in /data.
	If max_download_distance is increased, it will add to the already existing file.
	
	Parameters
	----------
	gaia_source : str
		Gaia source table (default: 'gaiadr3.gaia_source')
	max_download_distance : float
		Maximum distance in pc (default: 400)
	delete : bool
		Delete existing files before downloading
	"""
	if not os.path.isdir('data/'):
		os.mkdir('data/')
	
	file_hrdata = f"data/{gaia_source.split('.')[0]}_HR_parameters.fits"
	file_queries = f"data/{gaia_source.split('.')[0]}_queries.rdb"
	
	if delete:
		os.remove(file_hrdata)
		os.remove(file_queries)
	
	# Create parallax array to query separately, to not overload the Gaia server
	max_volume = max_download_distance**3
	volume_step = 4000000 # This should give around ~1 million stars in the first query
	volumes = np.arange(0, max_volume+volume_step, volume_step)[1:] # Minimum volume download is at least ~160 pc
	distances = volumes**(1/3)
	par = 1e3/distances # in mas
	
	# Check if the query was already performed
	queries = []
	if os.path.exists(file_queries):
		queries = pd.read_table(file_queries, header=None).to_numpy()
	
	with open(file_queries, "a") as f:
		# First the smallest distances
		parallax_filter = f"parallax>={par[0]}"
		if parallax_filter not in queries:
			all_res = query_gaia(parallax_filter, gaia_source)
			all_res.write(file_hrdata, overwrite=True) 
			
			f.write(parallax_filter + "\n")
		else:
			all_res = Table.read(file_hrdata)
		
		# Then loop over the rest up to approx. max_download_distance
		for p1, p2 in zip(par[1:], par[:-1]):
			parallax_filter = f"parallax>={p1} AND parallax<{p2}"
			if parallax_filter not in queries:
				res = query_gaia(parallax_filter, gaia_source)
				
				all_res = vstack([all_res, res])
				all_res.write(file_hrdata, overwrite=True) 
				
				f.write(parallax_filter + "\n")

if __name__ == '__main__':
	import argparse
	
	parser = argparse.ArgumentParser(description="Download Gaia HR diagram data.")
	parser.add_argument(
		"--dmax", type=float, default=400,
		help="Maximum distance to query in parsecs (default ~400), will always at least download up to ~160 pc.")
	parser.add_argument(
		"--gaia_source", type=str, default="gaiadr3.gaia_source",
		help="Gaia source table to query (default gaiadr3.gaia_source)")
	parser.add_argument(
		"--delete", action="store_true",
		help="Delete existing .fits files before downloading")

	args = parser.parse_args()

	download_gaia(
		gaia_source=args.gaia_source,
		max_download_distance=args.dmax,
		delete=args.delete)
