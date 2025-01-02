#!/bin/bash

# failure is a natural part of life
set -e

DATA_DIR=${1}

# The R package
doppel-describe \
    -p lightgbm \
    --language R \
    --data-dir "${DATA_DIR}"

doppel-describe \
    -p lightgbm \
    --language python \
    --data-dir "${DATA_DIR}"

doppel-test \
    --files "${DATA_DIR}/python_lightgbm.json,${DATA_DIR}/r_lightgbm.json" |
    tee out.log |
    cat
