#!/bin/bash

set -e -u -o pipefail

PACKAGE_NAME="${1}"
PYPI_URL="https://pypi.org"

if [ -f ./out.json ]; then
    echo "file './out.json' exists, not recreating it"
    exit 0
else
    echo "downloading PyPI details for package '${PACKAGE_NAME}'"
    curl \
        "${PYPI_URL}/pypi/${PACKAGE_NAME}/json" \
        -o ./out.json
fi

LATEST_VERSION=$(
    jq -r '."info"."version"' ./out.json
)

echo "latest version of '${PACKAGE_NAME}': ${LATEST_VERSION}"
echo "this release contains the following files:"

CSV_FILE="./${PACKAGE_NAME}.csv"
echo "file_name,size_bytes,download_url" > "${CSV_FILE}"

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
    echo "${file_name},${file_size_bytes},${download_url}" >> "${CSV_FILE}"
done
