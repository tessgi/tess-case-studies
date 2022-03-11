import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from __future__ import absolute_import  # noqa
from .run_nb import process_notebook
import os

PACKAGEDIR = os.path.abspath(os.path.dirname(__file__))


def process_notebook(notebook_filename):
    """Checks if an IPython notebook runs without error from start to finish."""
    with open(notebook_filename) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name="python3", allow_errors=True)
    ep.preprocess(nb, {"metadata": {"path": ""}})
    return
