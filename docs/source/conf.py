# Configuration file for the Sphinx documentation builder.
import sphinx_rtd_theme

# -- Project information
project = 'Heart disease prediction with advance technology'
copyright = '2025, Bình Phạm'
author = 'Kashish Agrawal'

release = '0.1'
version = '0.1.0'

# -- General configuration
extensions = [
    'nbsphinx',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx_rtd_theme',
    'sphinx_copybutton',
    'sphinx_gallery.load_style',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

templates_path = ['_templates']

# -- Options for HTML output
html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
highlight_language = 'python3'
epub_show_urls = 'footnote'

# Set the language to Vietnamese
language = 'vi'
