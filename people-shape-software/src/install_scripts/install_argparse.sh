#!/bin/bash

# [description]
#     Install 'argparse' from package managers
# [usage]
# ./install_scriptsinstall_feather.sh

pip install argparse

Rscript -e "install.packages('argparse', repos = 'http://cran.rstudio.com')"
