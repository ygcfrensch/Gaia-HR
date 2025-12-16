# Gaia-HR
Create HR diagrams from *Gaia* *G*, *G<sub>BP</sub>*, and *G<sub>RP</sub>* magnitudes.

The code allows you to overplot your favorite targets to check whether they lie on the Main Sequence.

## Installation & Requirements
The following instructions will git clone the repository:
```bash
git clone https://github.com/ygcfrensch/Gaia-HR
cd Gaia-HR
```

The code requires `numpy`, `pandas`, `matplotlib`, `astropy`, and `astroquery`, which are widely used and may already be installed. If not, or if you want to install in a separate environment (Python ≥ 3.10), you can run:

```bash
pip install -r requirements.txt
```

## Usage

## Comments & Suggestions
**Performed filtering** <br>
The *Gaia* magnitudes are filtered to include only the most reliable values. The following selection criteria are applied:
- `ruwe < 1.4`<br>
A value larger than 1.4 for the re-normalised unit weight error (RUWE) indicates a poor astrometric solution.
- `parallax_over_error ≥ 10`<br>
Ensures precise parallax measurements, corresponding to a distance uncertainty ≤ 10%.

**Choose your maximum distance carefully**
- Local up to 100 pc (≥ 10 mas) is clean for most purposes.
- Extended up to 200 pc (≥ 5 mas) gives a larger sample and allows you to see some evolved stars.
- Beyond 200 pc, an extinction correction is necessary, which is not included in this code.

**Choosing the colormap** <br>
By default, the colormap uses the General Stellar Parametrizer from Photometry (GSP-Phot) surface gravity (log g), as it helps distinguish MS and evolved stars and provides a rough indication of spectral type when other classifications are unavailable. Alternatively, the code allows color-coding stars by GSP-Phot metallicity ([M/H]).

## Credits
If you use `Gaia-HR`, please give credit to this work:
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

and add the following sentence within the acknowledgements section:
> This work made use of \texttt{Gaia-HR} (\url{https://github.com/ygcfrensch/Gaia-HR}).

Please also give credit to *Gaia* Data Release 3 ([Gaia Collaboration et al. 2023](https://ui.adsabs.harvard.edu/abs/2023A%26A...674A...1G/abstract)).
