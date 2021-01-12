# Recent Developments in LightGBM

## Description

> In this talk, attendees will learn about recent developments in LightGBM, a popular open source gradient boosting library. The talk's primary goal is to educate attendees about recent work that has been done to make LightGBM easier to install and use effectively.

> The talk will describe in detail a few recent additions to the library, including:
* CUDA-based GPU acceleration
* new options to make installation of a GPU-enabled Python package easier
* availability of the R package on CRAN
* new detailed documentation on hyperparameter tuning
* Dask integration for distributed training on large datasets

> Demos of the new (experimental) Dask integration will be shown. The talk will conclude with a summary of new features that are coming in the future, and a call for attendees who are interested to contribute their ideas, documentation, and code to LightGBM.


## Where this talk has been given:

* (virtual) [LA Big Data Science, Deep Learning, & AI meetup](https://www.chicagocloudconference.com/), January 2021 ([slides](https://docs.google.com/presentation/d/1eiom95e-rWtpj0qtZS9vjabc8lmRGgRko0VSneGaLKg/edit?usp=sharing))

<hr>

## Running the Demo Code

The code in this directory can be used to test LightGBM on Dask.

### Build an image

Build a docker image to run stuff in.

```shell
make docker-image
```

### Start Jupyter Lab

Run a notebook. The command below will print some stuff to the screen. Copy the notebook link from that output, change 8888 to 9000, and paste that URL into your browser.

This will run Jupyter Lab in a container that has the current working directory mounted in, so any files you create in Jupyter Lab will be written to your laptop's filesystem and still be there after shutting down the container.

```shell
make start-notebook
```

### Run Examples on Your Laptop

In Jupyter Lab, open `local.ipynb`. Run the code. Have fun!

### Run Examples on AWS

In a shell on your machine, run the following build and push an image that can be used for workers and the scheduler.

You'll need to [configure authentication details for AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html).

```shell
make cluster-image
make push-image
```

Once that's done, open `aws.ipynb` in Jupyter Lab and run it.

### Useful Links

* https://github.com/microsoft/LightGBM/pull/3515
* https://docs.aws.amazon.com/cli/latest/reference/ecr-public/
* https://docs.amazonaws.cn/en_us/AmazonECR/latest/public/docker-push-ecr-image.html
* https://github.com/dask/dask-docker
* https://docs.aws.amazon.com/AmazonECR/latest/public/public-registries.html
