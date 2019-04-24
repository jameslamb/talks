#!/bin/bash

DATA_DIR=${1:-doppel_results}
REPO_LOCATION=${2:-repos}

mkdir -p ${DATA_DIR}

for pkg in $(cat PACKAGES); do

    ./install_scripts/install_${pkg}.sh ${REPO_LOCATION}

    # The R package
    doppel-describe \
        -p ${pkg} \
        --language R \
        --data-dir ${DATA_DIR}

    doppel-describe \
        -p ${pkg} \
        --language python \
        --data-dir ${DATA_DIR}

done
