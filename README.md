## Generic Topic Modeling

Data and scripts for topic modeling projects using Gensim. Derived from the [Russian Blog Project](https://github.com/ghowa/russian-blogs).

Uses Python 3.9 and Jupyter notebooks for visualisation.

## Installation

0. Check out this repository

```
git init
git clone https://github.com/ghowa/russian-blogs.git
```
### Variant 1: Pip

1.1 Install required python packages

```
pip install -r requirements.txt
```

1.2 Activate qgrid:

```
jupyter nbextension enable --py --sys-prefix qgrid

# only required if you have not enabled the ipywidgets nbextension yet
jupyter nbextension enable --py --sys-prefix widgetsnbextension
```

### Variant 2: Anaconda

2.1 Install required python packages

```
conda env create -f environment.yml
```

## Usage

Start Jupyter notebook: 

```
jupyter notebook
```

A browser window will open. Select "corpus.ipynb" for browsing the corpus or "create_lda.ipynb" for creating a new topic model of the corpus.
