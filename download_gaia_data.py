import os
import numpy as np
import pandas as pd
from astroquery.gaia import Gaia
from astropy.table import Table, vstack

gaia_source='gaiadr3.gaia_source'
max_download_distance=1000

# Query Gaia for wanted parameters
def query_gaia(parallax_filter, gaia_source):
	"""
	query_gaia(parallax_filter, gaia_source='gaiadr3.gaia_source')
	parallax_filter: "parallax>=10", "parallax>=5 AND parallax<=10" etc.
	"""
	job_description = """SELECT parallax, logg_gspphot, teff_gspphot, phot_g_mean_mag, phot_rp_mean_mag, phot_bp_mean_mag, mh_gspphot, ruwe, parallax_over_error, ag_gspphot, ebpminrp_gspphot
	FROM %s
	WHERE %s AND ruwe<1.4 AND parallax_over_error>=10"""%(gaia_source, parallax_filter)
	print(parallax_filter)
    
	job = Gaia.launch_job_async(job_description)
	gtable = job.get_results()
    
	print('Number of stars in query: %i \n'%(len(gtable['parallax'])))
	return(gtable)
    
# Download necessary HR diagram data
def download_gaia(gaia_source, max_download_distance=1000, delete=False):
	"""
	download_gaia(gaia_source, max_download_distance=1000, delete=False)
	
	Downloads the necessary data into 'gaiadr#_HR_parameters.rdb'. 
	The data is downloaded in steps of volume, ensuring that the max_download_distance is included.
	The minimum volume downloaded starts at a distance of ~160 pc.
	If max_download_distance is increased, it will add to the already existing file.
	Queries are saved in steps to ensure no data loss. 
	
	gaia_source = 'gaiadr3.gaia_source'
	max_download_distance = 1000 (pc)
	delete: if True it deletes the existing data file
	
	Potential reasons to run:
	1. The data should include a larger distance (default max_download_distance=1000).
	2. There has been a new Gaia Data Release.
	3. gaiadr#_HR_parameters.rdb is corrupted (can also be downloaded from repo).	
	"""
	file_hrdata = f"{gaia_source.split('.')[0]}_HR_parameters.rdb"
	file_queries = f"{gaia_source.split('.')[0]}_queries.rdb"
	
	if delete:
		os.remove(file_hrdata)
		os.remove(file_queries)
	
	# Create parallax array to query separately, to not overload the Gaia server
	Vmax = max_download_distance**3
	Vstep = 4000000 # This should give around ~1 million stars in the first query
	V = np.arange(0, Vmax+Vstep, Vstep)[1:]
	dist = V**(1/3)
	par = 1e3/dist # in mas
	
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
				
# Download Gaia data in case the .rdb file does not exist
download_gaia(gaia_source, max_download_distance)
