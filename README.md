# TOX

Final Project for CS272: Introduction to Biomedical Informatics Research Methodology at Stanford University

Team: Ayush, Kevin, Shreyas, Tom

To get your local environment set up, run the following commands:
* `conda create -n tox python=3.9`
* `conda activate tox`
* `conda install -c conda-forge biopython`

## Data

The data folder contains data from previous papers, including ToxIBTL, ToxinPred, and NNTox.
Note that NNTox is not ccurently being used.

## EDA

The eda folder contains Python files that conduct exploratory data analysis. This includes the reading in and wrangling
of data into a standard format (i.e. sequence and toxic/non-toxic), identification of duplicate sequences, analysis of
sequence similarity, and the division of the data into training and test sets.

## Model Development

The model folder contains Jupyter notebooks used in the process of developing our ToxIN model.