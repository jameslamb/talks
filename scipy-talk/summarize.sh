#!/bin/bash

# [description]
#    Given a Python package tarball, summarize its contents.
#        - total size
#        - number of files
#        - longest filepath names
#        - largest files
#        - total size of files, grouped by file extension

set -e -u -o pipefail

DOWNLOAD_URL="https://files.pythonhosted.org/packages/5a/ac/b3b9aa2318de52e40c26ae7b9ce6d4e9d1bcdaf5da0899a691642117cf60/pandas-1.4.2.tar.gz"
LOCAL_FILE="pandas.tar.gz"

if [ -f "${LOCAL_FILE}" ]; then
    echo "file '${LOCAL_FILE}' exists, not re-downloading it"
else
    curl \
        -o "${LOCAL_FILE}" \
        ${DOWNLOAD_URL}
fi
PACKAGE_TARBALL="${LOCAL_FILE}"

#PACKAGE_TARBALL="${1}"
TEMP_PATH="$(pwd)/tmp-dir"

rm -rf ./tmp-dir
mkdir -p "${TEMP_PATH}"
cp "${PACKAGE_TARBALL}" "${TEMP_PATH}/package.tar.gz"

pushd "${TEMP_PATH}"

echo "checking compressed size..."
du --si ./package.tar.gz

echo "decompressing..."
tar -xzf ./package.tar.gz
rm ./package.tar.gz

echo "checking decompressed size..."
du -sh .

echo "summarizing contents"
# references:
# - https://unix.stackexchange.com/a/41552
# - 
ALL_FILE_EXTENSIONS=$(
    find \
        "${TEMP_PATH}" \
        -type f \
    | egrep \
        -o "\.[a-zA-Z0-9]+$" \
    | sort -u
)
echo "Found the following file extensions"
#echo " ${ALL_FILE_EXTENSIONS}"

echo "Summarizing file sizes by extension"
CSV_FILE="sizes.csv"
echo "extension,size" > "${CSV_FILE}"
for extension in ${ALL_FILE_EXTENSIONS}; do
    echo "  * ${extension}"
    SIZE=$(
        find \
            "${TEMP_PATH}" \
            -type f \
            -name "*${extension}" \
            -exec du -ch {} + \
        | grep total$ \
        | egrep -o '[0-9.]+[A-Z]+'
    )
    echo "${extension},${SIZE}" >> "${CSV_FILE}"
done

echo "  * (no extension)"
SIZE=$(
    find \
        "${TEMP_PATH}" \
        -type f \
        ! -name '*.*' \
        -exec du -ch {} + \
    | grep total$ \
    | egrep -o '[0-9.]+[A-Z]+'
)
echo "no-extension,${SIZE}" >> "${CSV_FILE}"

echo "done summarizing sizes"
