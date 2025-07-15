# Aviation

Simple (super low order) model of global aviation. Enjoy!

## Purpose
The purpose of this model is to estimate the global aircraft fleet requirement for meeting global passenger demands. The model consists of two simple equation whose variable inputs are given by a combination of real world data sources and guess-work. Feel free to expand the model's utility and fidelity.

## Developer Guide

### Dependencies

Install the dependencies using a virtual environment [venv](https://docs.python.org/3/library/venv.html) by running the following commands:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Documentation

The model's documentation was created using [MkDocs](https://mkdocs.org), the source files of which can be found in the `docs/` directory. The `mkdocs.yml` file allows customisation and configuration of the site. The documentation site can be activated locally using the following command:

```
mkdocs serve
```