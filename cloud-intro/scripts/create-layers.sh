#!/bin/bash

set -e

UPLOAD_DIR=$(pwd)/lambda-layers
TEMP_LAYER_DIR=$(pwd)/temp-layer-dir
mkdir -p "${TEMP_LAYER_DIR}"

echo "Creating 'pandas-layer'"
docker run \
    --rm \
    -v "${TEMP_LAYER_DIR}:/var/task" \
    lambci/lambda:build-python3.7 \
    pip install --no-deps -t python/lib/python3.7/site-packages pandas==0.24.1 pytz

pushd "${TEMP_LAYER_DIR}"
pushd python/lib/python3.7/site-packages/pytz
rm -r zoneinfo/Africa || echo "does not exist"
rm -r zoneinfo/Antarctica || echo "does not exist"
rm -r zoneinfo/Arctic || echo "does not exist"
rm -r zoneinfo/Asia || echo "does not exist"
rm -r zoneinfo/Atlantic || echo "does not exist"
rm -r zoneinfo/Australia || echo "does not exist"
rm -r zoneinfo/Brazil || echo "does not exist"
rm -r zoneinfo/Canada || echo "does not exist"
rm -r zoneinfo/Chile || echo "does not exist"
rm -r zoneinfo/Cuba || echo "does not exist"
rm -r zoneinfo/Egypt || echo "does not exist"
rm -r zoneinfo/Eire || echo "does not exist"
rm -r zoneinfo/Europe || echo "does not exist"
rm -r zoneinfo/Hongkong || echo "does not exist"
rm -r zoneinfo/Iceland || echo "does not exist"
rm -r zoneinfo/Indian || echo "does not exist"
rm -r zoneinfo/Iran || echo "does not exist"
rm -r zoneinfo/Israel || echo "does not exist"
rm -r zoneinfo/Jamaica || echo "does not exist"
rm -r zoneinfo/Japan || echo "does not exist"
rm -r zoneinfo/Kwajalein || echo "does not exist"
rm -r zoneinfo/Libya || echo "does not exist"
rm -r zoneinfo/Mexico || echo "does not exist"
rm -r zoneinfo/Navajo || echo "does not exist"
rm -r zoneinfo/Pacific || echo "does not exist"
rm -r zoneinfo/Poland || echo "does not exist"
rm -r zoneinfo/Portugal || echo "does not exist"
rm -r zoneinfo/Singapore || echo "does not exist"
rm -r zoneinfo/Turkey || echo "does not exist"
popd

zip \
    --exclude \*/tests/\* \*dist-info\* \*/__pycache__\* \
    -r pandas-layer.zip \
    python
mv ./*.zip "${UPLOAD_DIR}/"
rm -r python
popd
echo "Done creating 'pandas-layer'"

echo "Creating 'sklearn-layer'"
docker run \
    --rm \
    -v "${TEMP_LAYER_DIR}:/var/task" \
    lambci/lambda:build-python3.7 \
    pip install --no-deps -t python/lib/python3.7/site-packages/ joblib==0.14.1 scikit-learn==0.22.1

pushd "${TEMP_LAYER_DIR}"
zip \
    --exclude \*/tests/\* \*/test/\* \*dist-info\* \*/__pycache__\* \*/_build_utils\* \
    -r sklearn-layer.zip \
    python
mv ./*.zip "${UPLOAD_DIR}/"
rm -r python
popd
echo "Done creating 'sklearn-layer'"

echo "Creating 'lightgbm-layer'"
docker run \
    --rm \
    -v "${TEMP_LAYER_DIR}:/var/task" \
    lambci/lambda:build-python3.7 \
    pip install --no-deps -t python/lib/python3.7/site-packages/ lightgbm==2.3.1

pushd "${TEMP_LAYER_DIR}"
zip \
    --exclude \*/tests/\* \*/test/\* \*dist-info\* \*/__pycache__\* \*plotting\* \
    -r lightgbm-layer.zip \
    python
mv ./*.zip "${UPLOAD_DIR}/"
rm -r python
popd
echo "Done creating 'lightgbm-layer'"

echo "Creatting 'ticket-closure-lib-layer'"
mkdir -p "${TEMP_LAYER_DIR}/python/lib/python3.7/site-packages/"
cp -R ticket_closure_lib "${TEMP_LAYER_DIR}/python/lib/python3.7/site-packages/"
pushd "${TEMP_LAYER_DIR}"
zip \
    -r ticket-closure-lib-layer.zip \
    python
mv ./*.zip "${UPLOAD_DIR}/"
rm -r python
popd
echo "Done creating 'ticket-closure-lib-layer"
