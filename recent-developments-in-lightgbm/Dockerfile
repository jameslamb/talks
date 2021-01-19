FROM daskdev/dask-notebook:latest

# based on
# https://github.com/microsoft/LightGBM/pull/3515#pullrequestreview-543175003
ENV LIGHTGBM_DIR=${HOME}/LightGBM
ENV LIGHTGBM_URL="https://github.com/microsoft/LightGBM.git"

RUN apt update && \
    apt-get install -y \
        build-essential \
        cmake

RUN git clone \
    --recursive ${LIGHTGBM_URL} \
    --depth=1 \
    ${LIGHTGBM_DIR}

RUN conda install -y -c conda-forge \
    dask-cloudprovider \
    scikit-learn \
    numpy \
    pandas && \
    # install LightGBM
    cd ${LIGHTGBM_DIR}/python-package && \
    python setup.py sdist && \
    pip install dist/lightgbm*.tar.gz && \
    conda clean --all

WORKDIR /home/jovyan/testing
