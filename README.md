
# TOX

Final Project for CS272: Introduction to Biomedical Informatics Research Methodology at Stanford University

<br>

## Team

<kbd> Ayush </kbd> 
<kbd> Kevin </kbd> 
<kbd> Shreyas </kbd> 
<kbd> Tom </kbd>

<br>

To get your local environment set up, run the following commands:
* `conda create -n tox python=3.9`
* `conda activate tox`
* `conda install -c conda-forge biopython`
* `conda install -c pytorch pytorch`
* `conda install scikit-learn`
* 

To make the conda environment available in Jupyter notebook, run the following:
* `conda install -c anaconda ipykernel`
* `python -m ipykernel install --user --name=tox`

<br>
<br>

## Files

<br>

[![Button Data]][Data] 

    *Contains data from previous papers,* <br>
    *including **ToxIBTL**, **ToxDL** & **ToxinPred**.*

<br>

[![Button EDA]][EDA] 

    *Contains Python files for exploratory data analysis.*
 
    *This includes the reading in and wrangling of data into* <br>
    *a standard format ( sequences and toxic / non-toxic ),* <br>
    *identification of duplicate sequences, division of data* <br>
    *into training and test, as well as analysis of sequence* <br>
    *similarity.* 
    
<br>

[![Button CDHIT]][CDHIT] 

    *Contains data related to **[CD-HIT]**, which we use to* <br>
    *determine sequences that are at least `40%` similar.*

<br>

[![Button Model]][Model] 

    *Contains Jupyter notebooks used in the* <br>
    *process of developing our **ToxIN** model.*
    
    *The `/ToxIBTL/` folder contains* <br>
    *original code from **[ToxIBTL]**.*

<br>


<!----------------------------------------------------------------------------->

[ToxIBTL]: https://github.com/WLYLab/ToxIBTL
[CD-HIT]: http://weizhong-lab.ucsd.edu/cdhit_suite/cgi-bin/index.cgi?cmd=cd-hit


<!---------------------------------{ Folders }--------------------------------->

[CDHIT]: cdhit
[Model]: model
[Data]: data
[EDA]: eda


<!---------------------------------{ Buttons }--------------------------------->

[Button Model]: https://img.shields.io/badge/\/Model\/-F46D01?style=for-the-badge
[Button CDHIT]: https://img.shields.io/badge/\/CDHIT\/-EF2D5E?style=for-the-badge
[Button Data]: https://img.shields.io/badge/\/Data\/-008FC7?style=for-the-badge
[Button EDA]: https://img.shields.io/badge/\/EDA\/-00A98F?style=for-the-badge
