#!/bin/bash

# [description]
#     Install 'sparkR' and 'pyspark' from package managers
# [usage]
# ./install_scriptsinstall_spark.sh

pip install pyspark

Rscript -e "install.packages('SparkR', repos = 'http://cran.rstudio.com')"
