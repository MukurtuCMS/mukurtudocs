# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mukurtu Support'
copyright = '2024, Mukurtu'
author = 'Mukurtu'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx_rtd_theme',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.youtube',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['source/_static']
html_css_files = [
    'css/mukurtu.css'
]
html_logo = "logo.png"
html_favicon = 'favicon.ico'
html_theme_options = {
    'style_external_links': True,
    'style_nav_header_background': '#343131',
    'logo_only': False,
    'display_version': True,
}
