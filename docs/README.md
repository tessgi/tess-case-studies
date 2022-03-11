<a href="https://github.com/tessgi/tess-case-studies/actions/workflows/tests.yml"><img src="https://github.com/tessgi/tess-case-studies/workflows/pytest/badge.svg" alt="Test status"/></a> [![Generic badge](https://img.shields.io/badge/documentation-live-blue.svg)](https://tessgi.github.io/tess-case-studies)

# TESS Case Studies

This site contains some of the case studies assembled by the [TESS Science Support Center](https://heasarc.gsfc.nasa.gov/docs/tess/) to demonstrate how to do some useful and unusual data analysis with NASA TESS data. Click the menu to navigate through some of our case studies.

## How to run a Case Study

If you'd like to run a case study locally you can download the notebooks [here](https://github.com/tessgi/tess-case-studies/tree/main/docs/notebooks/) and run them locally. You will usually need some tools (e.g. `lightkurve`) installed to run these notebooks. You can read the requirements for the notebooks [here](https://github.com/tessgi/tess-case-studies/blob/main/pyproject.toml). If you struggle to run the notebooks locally, try following the install instructions at the bottom of this page.

## Identifying Issues with a Case Study

If you think there might be something wrong with a case study that you'd like to discuss, or you think you'd like to talk about improvements, please [open an issue](https://github.com/tessgi/tess-case-studies/issues) on the [GitHub repository](https://github.com/tessgi/tess-case-studies) for `tess-case-studies`. We'd be very happy to discuss further!

### Contributing a Case Study

If you would like to contribute a case study notebook you should first fork the [`tess-case-studies` project](https://github.com/tessgi/tess-case-studies) and install it, probably using `poetry`. From the `tess-case-studies` directory use

```
python -m pip install --upgrade pip
python -m pip install poetry
poetry install
```

to install the package. You can then add your notebook to the `docs/notebooks/` directory. If you need any additional packages to run your notebook you can add them using

```
poetry add newpackage
```

(See the [`poetry`](https://python-poetry.org/) documentation for further information.) Next, add a link to your page in the `mkdocs.yml` file under `nav`, see below:

```
nav:
    - Home : README.md
    - Case Studies:
      - notebooks/pixel-level-detrending.ipynb
      - notebooks/my-new-case-study.ipynb
```

Check your notebook compiles locally using

```
make pytest
```

If this fails, you should fix the issue locally in your notebook (try running it in `jupyter-lab` and finding where it fails.) If the notebook passes, you can test that it renders nicely using

```
make serve
```

Wait for this to finish, and then navigate to http://127.0.0.1:8000/ on your browser to see that it renders. This command runs all the notebooks, so it might take a few minutes.

Once this runs, open a [pull request](https://github.com/tessgi/tess-case-studies/pulls) against `tess-case-studies`, and we will review the submission.
