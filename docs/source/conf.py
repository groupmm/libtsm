# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import sys

DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
assert os.path.exists(os.path.join(DIR, 'libtsm'))
sys.path.insert(0, DIR)

from importlib.metadata import version

# -- Project information -----------------------------------------------------

project = 'libtsm'
copyright = '2021-2026, Sebastian Rosenzweig, Simon Schwär, Jonathan Driedger, Meinard Müller'
author = 'Sebastian Rosenzweig, Simon Schwär, Jonathan Driedger, Meinard Müller'

# reading version
version = release = version(project)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',   # documentation based on docstrings
    'sphinx.ext.napoleon',  # for having google/numpy style docstrings
    'sphinx.ext.viewcode',  # link source code
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme  # noqa

html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_use_index = True
html_use_modindex = True

html_logo = os.path.join(html_static_path[0], 'libtsm.png')

html_theme_options = {'logo_only': True}


def remove_module_docstring(app, what, name, obj, options, lines):
    if what == "module":
        del lines[:]


def setup(app):
    app.connect('autodoc-process-docstring', remove_module_docstring)
