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

Lastly you will need to generate the `*.ipynb` notebook files from the `*.py` git friendly source files using `jupytext`.

If you are using JupyterLab then this is not really necessary as you will be able to right-click the `*.py` files and open them as notebooks (on saving, the notebook files will also be created). In JupyterLab, `jupytext` will automatically keep the `*.py` and `*.ipynb` files in sync.

### Optional - Generating and syncing notebook files for use in an IDE (ie. not JupyterLab)

If you are using a different environment for editing notebooks (eg. PyCharm or VSCode) then it may be necessary to create the `*.ipynb` files manually using the following command:

```shell
jupytext --sync *.py
```

You will then be able to work in the `*.ipynb` files directly in your IDE and take advantage of the IDE features.

**NB. You should note that saving the `*.ipynb` files in your editor will not automatically update the `*.py` files and vice versa (as happens in JupyterLab) and that you will need to run the following sync command before committing changes to Git:**

```shell
jupytext --sync *.ipynb
```

Often it will not matter if you run the sync command using `*.ipynb` or `*.py`, but if you create a new `*.ipynb` notebook then in order to generate the corresponding `*.py` file, then it will matter as the `*.py` file will not exist yet.

Similarly, if you do not yet have `*.ipynb` notebook files (eg. after cloning the repository) then it is necessary to specify `*.py` in the sync command.

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

