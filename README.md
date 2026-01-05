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
The Jupyter notebook `Gaia-HR_Figure.ipynb` provides a step-by-step example of how to generate an HR diagram with this code.

<img width="2159" height="1749" alt="HR_diagram_example" src="https://github.com/user-attachments/assets/407cd62f-e66a-4940-a987-592cee6f7b36" />


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
@ARTICLE{2025arXiv251011703F,
       author = {{Frensch}, Yolanda G.~C. and {Bouchy}, Fran{\c{c}}ois and {Lo Curto}, Gaspare and {L'Heureux}, Alexandrine and {de Lima Gomes}, Roseane and {Faria}, Jo{\~a}o and {Dumusque}, Xavier and {Malo}, Lison and {Cointepas}, Marion and {Srivastava}, Avidaan and {Bonfils}, Xavier and {Delgado-Mena}, Elisa and {Nari}, Nicola and {Al Moulla}, Khaled and {Allart}, Romain and {Almenara}, Jose M. and {Artigau}, {\'E}tienne and {Barkaoui}, Khalid and {Baron}, Fr{\'e}d{\'e}rique and {Barros}, Susana C.~C. and {Benneke}, Bj{\"o}rn and {Bryan}, Marta and {Cadieux}, Charles and {Canto Martins}, Bruno L. and {de Castro Le{\~a}o}, Izan and {Castro-Gonz{\'a}lez}, Amadeo and {Cloutier}, Ryan and {Collins}, Karen A. and {Cowan}, Nicolas B. and {Cristo}, Eduardo and {De Medeiros}, Jose R. and {Delfosse}, Xavier and {Doyon}, Ren{\'e} and {Ehrenreich}, David and {Fajardo-Acosta}, Sergio B. and {Forveille}, Thierry and {Gan}, Tianjun and {Gomes da Silva}, Jo{\~a}o and {Gonz{\'a}lez Hern{\'a}ndez}, Jonay I. and {Grieves}, Nolan and {Howell}, Steve and {Lafreni{\`e}re}, David and {Lovis}, Christophe and {Melo}, Claudio and {Messamah}, Lina and {Mignon}, Lucile and {Mordasini}, Christoph and {Nielsen}, Louise D. and {Osborn}, Ares and {Parc}, L{\'e}na and {Pepe}, Francesco and {Piaulet-Ghorayeb}, Caroline and {Rebolo}, Rafael and {Rowe}, Jason and {Santos}, Nuno C. and {S{\'e}gransan}, Damien and {Stassun}, Keivan G. and {Striegel}, Stephanie and {Su{\'a}rez Mascare{\~n}o}, Alejandro and {Udry}, St{\'e}phane and {Ulmer-Moll}, Sol{\`e}ne and {Valencia}, Diana and {Vaulato}, Valentina and {Wade}, Gregg and {Watkins}, Cristilyn N.},
        title = "{TOI-3288 b and TOI-4666 b: two gas giants transiting low-mass stars characterised by NIRPS}",
      journal = {arXiv e-prints},
     keywords = {Earth and Planetary Astrophysics},
         year = 2025,
        month = oct,
          eid = {arXiv:2510.11703},
        pages = {arXiv:2510.11703},
          doi = {10.48550/arXiv.2510.11703},
archivePrefix = {arXiv},
       eprint = {2510.11703},
 primaryClass = {astro-ph.EP},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2025arXiv251011703F},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```

and add this line where relevant:
> This work made use of \texttt{Gaia-HR} (\url{https://github.com/ygcfrensch/Gaia-HR}).

`Gaia-HR` builds on the following works, please cite them too:
- *Gaia* DR3 ([Gaia Collaboration et al. 2023](https://ui.adsabs.harvard.edu/abs/2023A%26A...674A...1G/abstract))
- *Gaia* GSP-Phot ([R. Andrae et al. 2023](https://www.aanda.org/articles/aa/full_html/2023/06/aa43462-22/aa43462-22.html))
