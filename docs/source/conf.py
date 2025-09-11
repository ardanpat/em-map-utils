# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sys
from pathlib import Path

sys.path.insert(0, str(Path('..', '..').resolve()))

# Needed for autoapi
def contains(seq, item):
    return item in seq

def prepare_jinja_env(jinja_env) -> None:
    jinja_env.tests["contains"] = contains

autoapi_prepare_jinja_env = prepare_jinja_env


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'em_map_utils'
copyright = '2025, Ardan Patwardhan'
author = 'Ardan Patwardhan'
release = '0.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'autoapi.extension',
]

# Setup autoapi
# Thanks to: https://bylr.info/articles/2022/05/10/api-doc-with-sphinx-autoapi/#basic-macro-setup
autoapi_dirs = ['../../em_map_utils']
autoapi_type = "python"
autoapi_template_dir = "_templates/autoapi"
autoapi_keep_files = True
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",
]
autodoc_typehints = "signature"

autosummary_generate = True
rst_prolog = """
.. role:: summarylabel
"""
html_css_files = [
    "css/custom.css",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
