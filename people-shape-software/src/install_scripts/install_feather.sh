#!/bin/bash

# [description]
#     Install 'feather' from package managers
# [usage]
# ./install_scriptsinstall_feather.sh $(pwd)/repos

pip install feather-format

Rscript -e "install.packages('feather', repos = 'http://cran.rstudio.com')"
