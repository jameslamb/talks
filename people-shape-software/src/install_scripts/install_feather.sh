#!/bin/bash

# [description]
#     Install 'feather' from source
# [usage]
# ./install_scriptsinstall_feather.sh $(pwd)/repos

REPO_LOCATION=${1}

pushd ${REPO_LOCATION}
    
    git clone \
        --depth=1 \
        https://github.com/wesm/feather.git

    echo "installing python"
    
    pushd $(pwd)/feather/python

        python setup.py install

    popd

    echo "done installing python"

    echo "install R"

    pushd $(pwd)/feather/R
        R CMD INSTALL .
    popd

    echo "done installing R"

popd
