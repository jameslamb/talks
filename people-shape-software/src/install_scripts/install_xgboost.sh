#!/bin/bash

# [description]
#     Install 'feather' from source
# [usage]
# ./install_scripts/install_xgboost.sh $(pwd)/repos

REPO_LOCATION=${1}

pushd ${REPO_LOCATION}
    
    export CC=/usr/local/bin/gcc-8
    export CXX=/usr/local/bin/g++-8

    # git clone \
    #    --depth=1 \
    #    --recursive \
    #    https://github.com/dmlc/xgboost.git

    echo "installing python"
    
    pushd $(pwd)/xgboost

        mkdir build
        cd build
        cmake ..
        make -j4

        pushd $(pwd)/python-package

            python setup.py install

        popd

    popd

    echo "done installing python"

    echo "install R"

    pushd $(pwd)/xgboost/R-package
        R CMD INSTALL .
    popd

    echo "done installing R"

popd
