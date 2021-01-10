#!/bin/bash

# failure is a natural part of life
set -e

DATA_DIR=${1}

# The R package
doppel-describe \
    -p argparse \
    --language R \
    --data-dir "${DATA_DIR}"

doppel-describe \
    -p argparse \
    --language python \
    --data-dir "${DATA_DIR}"

doppel-test \
    --files "${DATA_DIR}/python_argparse.json,${DATA_DIR}/r_argparse.json" \
    | tee out.log \
    | cat
