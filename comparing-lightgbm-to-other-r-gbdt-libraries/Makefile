
IMAGE_NAME=r-gbdt-demo

build:
	docker build \
		--no-cache \
		-f Dockerfile \
		-t ${IMAGE_NAME} \
		.

run:
	docker run --rm \
		-v $$(pwd):/home/rstudio/demo \
		-p 127.0.0.1:8787:8787 \
		-e ROOT=TRUE \
		-e DISABLE_AUTH=true \
		${IMAGE_NAME}
