#!/bin/bash

# [description]
#     Install 'feather' from source
# [usage]
# ./install_scripts/install_xgboost.sh $(pwd)/repos

pip install xgboost

Rscript -e "install.packages('xgboost', repos = 'http://cran.rstudio.com')"
