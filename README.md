# TOX

Final Project for CS272: Introduction to Biomedical Informatics Research Methodology at Stanford University

Team: Ayush, Kevin, Shreyas, Tom

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

## Data

The data folder contains data from previous papers, including ToxIBTL, ToxDL, and ToxinPred.

## EDA

The eda folder contains Python files that conduct exploratory data analysis. This includes the reading in and wrangling
of data into a standard format (i.e. sequence and toxic/non-toxic), identification of duplicate sequences, analysis of
sequence similarity, and the division of the data into training and test sets.

## CDHIT

The cdhit folder contains data related to
[CD-HIT](http://weizhong-lab.ucsd.edu/cdhit_suite/cgi-bin/index.cgi?cmd=cd-hit), which we use to determine sequences
that are at least 40% similar.


## Model Development

The model folder contains Jupyter notebooks used in the process of developing our ToxIN model.
The ToxIBTL folder contains original code from [ToxIBTL](https://github.com/WLYLab/ToxIBTL).