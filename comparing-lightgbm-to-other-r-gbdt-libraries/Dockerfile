FROM rocker/rstudio:4.0.5

COPY --chown=rstudio:rstudio ./rstudio-prefs.json /home/rstudio/.config/rstudio/rstudio-prefs.json

RUN Rscript -e "install.packages(c('lightgbm', 'remotes', 'xgboost'))" && \
    Rscript -e "remotes::install_github(repo = 'catboost/catboost', subdir = 'catboost/R-package', ref = 'v0.25.1')"
