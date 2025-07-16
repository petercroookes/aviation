# Aviation

Simple (super low order) model of global aviation. Enjoy!

## Purpose
The purpose of this model is to estimate the global aircraft fleet requirement for meeting global passenger demands. The model consists of two simple equation whose variable inputs are given by a combination of real world data sources and guess-work. Feel free to expand the model's utility and fidelity.

## Developer Guide

### Dependencies

This repository uses [uv](https://docs.astral.sh/uv/) for project and package management. The file [`pyproject.toml`](pyproject.toml) defines the dependency bounds and [`uv.lock`](uv.lock) specifies the locked environment.
To create the virtual environment from lockfile, ensure you have uv installed and run the following command:

```
uv sync
```

## Documentation

The model's documentation was created using [MkDocs](https://mkdocs.org), the source files of which can be found in the `docs/` directory. The `mkdocs.yml` file allows customisation and configuration of the site. The documentation site can be activated locally using the following command:

```
mkdocs serve
```