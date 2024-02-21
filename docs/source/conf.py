# noqa: INP001
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))
sys.path.insert(0, os.path.abspath("../../mwrpy/"))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "MWRpy"
copyright = "2024, Institute for Geophysics and Meteorology, University of Cologne"
author = "Institute for Geophysics and Meteorology, University of Cologne"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.imgmath",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
]

templates_path = ["_templates"]
exclude_patterns = ["_temp/*"]
autodoc_member_order = "bysource"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

napoleon_google_docstring = True
