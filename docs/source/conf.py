import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "rheedium"
copyright = "2024"
author = "Debangshu Mukherjee"

# The full version, including alpha/beta/rc tags
release = '2025.01.28'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Napoleon settings for custom docstring format
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True
napoleon_attr_annotations = True
napoleon_custom_sections = [
    'Flow',
    'Description'
]

# Type hints settings
autodoc_typehints = 'description'
autodoc_typehints_format = 'short'
python_use_unqualified_type_names = True

# Intersphinx mapping for external references
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'jax': ('https://jax.readthedocs.io/en/latest/', None),
}

# Custom CSS to improve type hint rendering
html_css_files = [
    'custom.css',
]

html_theme = "sphinx_rtd_theme"
