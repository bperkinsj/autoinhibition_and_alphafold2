# Autoinhibition and AlphaFold2
This repository contains the main component of the pipeline for comparing AlphaFold2-generated predictions to experimental structures.

## Install the environment
Make sure you have [Anaconda](https://www.anaconda.com/download) installed.

To install the ```rmsd_snek``` environment, follow the documentation on [creating an environment from an environment.yml file](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file).

## Running the pipeline
The first step of the pipeline is the ```Snakefile``` in the ```project_pipeline``` folder. The pipeline requires a tab-separated (tsv) file in the format

| uniprot | region_1 | region_2 |
| ---     | ---      | ---      | 
| P28583  | 15-139   | 211-412  | 

where "uniprot" is the UniProt ID, "region_1" is the sequence range of the inhibitory module, and "region_2" is the sequence range of the functional domain. It also requires all of the AlphaFold-predicted files to be placed in ```data/Alphafold_cif```.

The final output will be to the file ```rmsds.tsv```.