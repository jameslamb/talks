FROM daskdev/dask-notebook:latest

# based on
# https://github.com/microsoft/LightGBM/pull/3515#pullrequestreview-543175003
ENV LIGHTGBM_DIR=${HOME}/LightGBM
ENV LIGHTGBM_URL="https://github.com/microsoft/LightGBM.git"
ENV LIGHTGBM_COMMIT="78d31d9ae34c9c8ab2b0f8704c6962c8d3510062"

RUN apt update && \
    apt-get install -y \
        build-essential \
        cmake

RUN git clone --recursive --depth=1 ${LIGHTGBM_URL} ${LIGHTGBM_DIR} && \
    cd ${LIGHTGBM_DIR} && \
    git checkout ${LIGHTGBM_COMMIT}

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