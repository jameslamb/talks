#!/bin/bash

set -e -u -o pipefail

PACKAGE_NAME="${1}"
PYPI_URL="https://pypi.org"

curl \
    "${PYPI_URL}/pypi/${PACKAGE_NAME}/json" \
    -o ./out.json

LATEST_VERSION=$(
    jq -r '."info"."version"' ./out.json
)

echo "latest version of '${PACKAGE_NAME}': ${LATEST_VERSION}"
echo "this release contains the following files:"

for file_info in $(
        jq \
            -r \
            --arg version "${LATEST_VERSION}" \
            '."releases"[$version] | keys[] as $k | "\(.[$k])"' \
            ./out.json
    );
do
    echo "----"
    file_name=$(
        echo ${file_info} \
        | jq -r '."filename"'
    )
    file_size_bytes=$(
        echo ${file_info} \
        | jq -r '."size"'
    )
    download_url=$(
        echo ${file_info} \
        | jq -r '."url"'
    )
    echo "  * (${file_size_bytes}) ${file_name}"
done
