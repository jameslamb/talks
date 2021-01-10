#!/bin/bash

# failure is a natural part of life
set -e

DATA_DIR=${1}

# The R package
doppel-describe \
    -p SparkR \
    --language R \
    --data-dir "${DATA_DIR}"

doppel-describe \
    -p pyspark \
    --language python \
    --data-dir "${DATA_DIR}"

doppel-test \
    --files "${DATA_DIR}/python_pyspark.json,${DATA_DIR}/r_sparkR.json" \
    | tee out.log \
    | cat
