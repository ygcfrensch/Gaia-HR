# Gaia-HR
Create HR diagrams from *Gaia* *G*, *G<sub>BP</sub>*, and *G<sub>RP</sub>* magnitudes.

The code allows you to overplot your favorite targets to check whether they lie on the main sequence and provides an estimate of their effective temperatures.

## Installation
To clone the repo from GitHub:
```bash
git clone https://github.com/ygcfrensch/Gaia-HR
cd Gaia-HR
```

The code uses `numpy`, `pandas`, `matplotlib`, `astropy`, and `astroquery`. If they’re not installed, or if you prefer a separate environment (Python ≥ 3.10), run:
```bash
pip install -r requirements.txt
```

## Usage
1. Download the necessary *Gaia* data. The script queries the *Gaia* archive in increasing volume steps and saves the results to a .fits file. Run:
```bash
python download_gaia_data.py
```
to query stars up to ~400 pc (~260 MB). You can adjust the maximum distance or select a different *Gaia* DR; use `-h` to see the available options. The download may take some time, but can run in parallel while you start creating your first HR plot.

## Comments & Suggestions
**Performed filtering** <br>
The *Gaia* magnitudes are filtered to include only the most reliable values. The following selection criteria are applied:
- `ruwe < 1.4`<br>
A value larger than 1.4 for the re-normalised unit weight error (RUWE) indicates a poor astrometric solution.
- `parallax_over_error ≥ 10`<br>
Ensures precise parallax measurements, corresponding to a distance uncertainty ≤ 10%.

**Choose your maximum distance carefully** <br>
This code applies dereddening using the General Stellar Parametrizer from Photometry (GSP-Phot) parameters `ag_gspphot` and `ebpminrp_gspphot`. However, as these estimates are model-based, the corrections should be treated with caution, particularly for distant, faint, or crowded stars. 
- Local up to 100 pc (≥ 10 mas) is clean for most purposes.
- Extended up to 200 pc (≥ 5 mas) gives a larger sample and allows you to see some evolved stars.
- Beyond 200 pc, extinction corrections become important.

Note: the code provides the option to skip dereddening.

**Choosing the colormap** <br>
By default, the colormap uses the GSP-Phot surface gravity log $g$, as it helps distinguish main sequence and evolved stars and provides a rough indication of spectral type when other classifications are unavailable. Alternatively, the code allows color-coding stars by GSP-Phot metallicity [M/H].

## Credits
Please include the following citation if you use `Gaia-HR` in your work or research:
```
@ARTICLE{2025A&A...700A.118F,
       author = {{Frensch}, Y.~G.~C. and {Bouchy}, F. and {Lo Curto}, G. and {Ulmer-Moll}, S. and {Sousa}, S.~G. and {Santos}, N.~C. and {Stassun}, K.~G. and {Watkins}, C.~N. and {Chakraborty}, H. and {Barkaoui}, K. and {Battley}, M. and {Ceva}, W. and {Collins}, K.~A. and {Daylan}, T. and {Evans}, P. and {Faria}, J.~P. and {Farret Jentink}, C. and {Fontanet}, E. and {Frid{\'e}n}, E. and {Furesz}, G. and {Gillon}, M. and {Grieves}, N. and {Hellier}, C. and {Jehin}, E. and {Jenkins}, J.~M. and {Kwok}, L.~K.~W. and {Latham}, D.~W. and {Lavie}, B. and {Law}, N. and {Mann}, A.~W. and {Murgas}, F. and {Palle}, E. and {Parc}, L. and {Pepe}, F. and {Popowicz}, A. and {Pozuelos}, F.~J. and {Radford}, D.~J. and {Relles}, H.~M. and {Revol}, A. and {Ricker}, G. and {Seager}, S. and {Shinde}, M. and {Steiner}, M. and {Strakhov}, I.~A. and {Tan}, T.-G. and {Tavella}, S. and {Timmermans}, M. and {Tofflemire}, B. and {Udry}, S. and {Vanderspek}, R. and {Vaulato}, V. and {Winn}, J.~N. and {Ziegler}, C.},
        title = "{Three hot Jupiters transiting K-dwarfs with significant heavy element masses}",
      journal = {\aap},
     keywords = {techniques: photometric, techniques: radial velocities, planets and satellites: general, stars: individual: TOI-2969, stars: individual: TOI-2989, stars: individual: TOI-5300, Earth and Planetary Astrophysics},
         year = 2025,
        month = aug,
       volume = {700},
          eid = {A118},
        pages = {A118},
          doi = {10.1051/0004-6361/202553879},
archivePrefix = {arXiv},
       eprint = {2506.04923},
 primaryClass = {astro-ph.EP},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2025A&A...700A.118F},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```

and add this line where relevant:
> This work made use of \texttt{Gaia-HR} (\url{https://github.com/ygcfrensch/Gaia-HR}).

`Gaia-HR` builds on the following works, please cite them too:
- *Gaia* DR3 ([Gaia Collaboration et al. 2023](https://ui.adsabs.harvard.edu/abs/2023A%26A...674A...1G/abstract))
- *Gaia* GSP-Phot ([R. Andrae et al. 2023](https://www.aanda.org/articles/aa/full_html/2023/06/aa43462-22/aa43462-22.html))
