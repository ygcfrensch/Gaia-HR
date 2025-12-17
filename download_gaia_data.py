import os
import numpy as np
from astroquery.gaia import Gaia
from astropy.table import Table

gaia_source='gaiadr3.gaia_source'

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
    
    new_dict = {}
    for ky in gtable.keys():
    	new_dict[ky] = gtable[ky].value
	print('Number of stars in query: %i \n'%(len(new_dict['parallax'])))
	return(gtable)
	
def save_results(all_res):
	"""
	save_results(all_res)
	all_res: table to save
	"""
	rdb_res = Table(all_res)
	rdb_res.write('%s_HR_parameters.rdb'%(gaia_source.split('.')[0]), overwrite=True) 
    
# Download necessary HR diagram data
def download_gaia(gaia_source, max_download_distance=1000, delete=False):
	"""
	download_gaia(gaia_source, max_download_distance=1000, delete=False)
	
	Downloads the necessary data into 'gaiadr#_HR_parameters.rdb'.
	gaia_source = 'gaiadr3.gaia_source'
	max_download_distance = 1000 (pc)
	delete: If true it deletes the existing data file
	
	Potential reasons to run:
	1. The data should include a larger distance (default dmax=1000).
	2. There has been a new Gaia Data Release.
	3. gaiadr#_HR_parameters.rdb is corrupted (can instead be downloaded from repo).	
	"""
	# Separate queries to not overload Gaia server
	dist = ((max_download_distance**3 * np.linspace(0, 1, int((max_download_distance**3)/4e6)))**(1/3))[1:]
	par = 1e3/dist # in mas

	# First smallest distances
	parallax_filter = f"parallax>={par[0]}"
	all_res = query_gaia(parallax_filter, gaia_source)
	save_results(all_res, done_queries)
	
	# Then loop over the rest
	for p1, p2 in zip(par[1:], par[:-1]):
		parallax_filter = f"parallax>={p1} AND parallax<{p2}"
		res = query_gaia(parallax_filter, gaia_source)
		for ky in all_res.keys():
			all_res[ky] = np.append(all_res[ky], res[ky])
		save_results(all_res, done_queries)	

# Download Gaia data in case the .rdb file does not exist
file_hrdata = gaia_source.split('.')[0]
if not os.path.exists(file_hrdata):
	query_gaia(gaia_source)
