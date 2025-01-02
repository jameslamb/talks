#!/bin/bash

# failure is a natural part of life
set -e

DATA_DIR=${1}

# The R package
doppel-describe \
    -p xgboost \
    --language R \
    --data-dir "${DATA_DIR}"

doppel-describe \
    -p xgboost \
    --language python \
    --data-dir "${DATA_DIR}"

doppel-test \
    --files "${DATA_DIR}/python_xgboost.json,${DATA_DIR}/r_xgboost.json" |
    tee out.log |
    cat
