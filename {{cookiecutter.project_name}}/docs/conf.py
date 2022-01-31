"""Sphinx configuration."""
from datetime import datetime

project = "{{cookiecutter.friendly_name}}"
author = "{{cookiecutter.author}}"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
<<<<<<< HEAD
    "sphinx_click"
=======
    "sphinx.ext.viewcode",
    "sphinx_click",
    "sphinx_rtd_theme",
>>>>>>> b0866a9... if you more chances
]
autodoc_typehints = "description"
html_theme = "sphinx_rtd_theme"
