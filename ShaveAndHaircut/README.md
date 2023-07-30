# Shave and Haircut

## Dependencies

- [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html) or [Miniconda](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/index.html)

## Setup

An `environment.yml` file is provided to get you up and running with a Conda environment quickly. From this directory run:

```shell
conda env create -f environment.yml
```

This will create a new environment called `shave-and-haircut` with the required dependencies installed.

Activate the environment with:

```shell
conda activate shave-and-haircut
```

## Updating dependencies

**NB. do not add dependencies directly using `conda install` as they will not be automatically saved to the `environment.yml` file for others to use**

Add or remove dependencies from the `dependencies` list in `environment.yml` then run the following command to update the environment:

```shell
conda env update --file environment.yml --prune
```

**NB. it may be necessary to restart the Jupyter server (or at least the kernel) in order to pick up the changes in the enviroment**


## Starting the JupyterLab server

After setting up and activating the Conda environment, run the following command to start the JupyterLab server:

```shell
jupyter lab
```

