#!/bin/bash

PKG=${1}
DATA_DIR=${2:-doppel_results}

mkdir -p "${DATA_DIR}"


"./install_scripts/install_${PKG}.sh"

"./test_scripts/test_${PKG}.sh" "${DATA_DIR}"
