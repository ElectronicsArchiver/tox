# Extract embeddings:

First, make sure you have pytorch and fair-esm installed. You can either install them directly or use the pipenv file (instructions in testESM)
To install directly: 
> pip install fair-esm

> pip install torch torchvision

Once you have the packages installed, call extract.py to produce embeddings:
> python extract.py esm1b_t33_650M_UR50S {examplefile.fasta} {output directory} --include mean

Example: 
> python extract.py esm1b_t33_650M_UR50S data/final_sample.fasta data/final_sample_embeddings/ --include mean

Output files will be stored in the output directory. To extract the embedding from a file, run:
> t = torch.load('/data/final_sample_embeddings/UniRef50_A0A1D5ZRM3.pt')

> embedding = t['mean_representations'][33]

Note: 
1. The embedding will be a tensor of dimension 1280. 
2. The script will generate a copy of the input fasta file with sequences captialized, since this format is required for processing.

# testESM
Testing the FB embedding generator. 

# Instructions:
In order to test the FB embedding generator, make sure you're in the testESM directory. 

1. The first time you run testESM, run $ pipenv install to install required packages. 
2. Run $ pipenv shell to activate the pipenv shell
3. Run $ python esmTest.py to generate embeddings for preset sequences.
