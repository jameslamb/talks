# Testing LightGBM on Dask

The code in this directory can be used to test LightGBM on Dask.

## Build an image

Build a docker image to run stuff in.

```shell
make docker-image
```

## Start Jupyter Lab

Run a notebook. The command below will print some stuff to the screen. Copy the notebook link from that output, change 8888 to 9000, and paste that URL into your browser.

This will run Jupyter Lab in a container that has the current working directory mounted in, so any files you create in Jupyter Lab will be written to your laptop's filesystem and still be there after shutting down the container.

```shell
make start-notebook
```

## Run Examples on Your Laptop

In Jupyter Lab, open `local.ipynb`. Run the code. Have fun!

## Run Examples on AWS

In a shell on your machine, run the following to push the docker image to the ECR Public Repository.

```shell
make push-image
```


