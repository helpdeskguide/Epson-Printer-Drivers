# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths that contain custom modules here
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Epson Printer Driver Setup'
copyright = '2025, Epson'
author = 'Epson Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "Download and Install Epson Printer Drivers – Step-by-Step Guide"

# Optional short title (e.g., for nav bar)
html_short_title = "Epson Driver Install"

# Favicon (place favicon.ico in root or _static directory if you have one)
html_favicon = 'favicon.ico'

# Choose a theme (e.g., 'alabaster', 'sphinx_rtd_theme', etc.)
# html_theme = 'sphinx_rtd_theme'  # Uncomment if using ReadTheDocs theme

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Paths to templates and static files
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment and add files if needed

# Patterns to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
