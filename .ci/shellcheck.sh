#!/bin/bash

echo "checking shell scripts with 'shellcheck'"
shell_scripts=$(git ls-files | grep -E '\.sh$')

for f in ${shell_scripts}; do
    echo "    * ${f}"
    shellcheck \
        --norc \
        --exclude=SC2002,SC2045 \
            ${f} \
    || exit 1
done
echo "done checking shell scripts"
