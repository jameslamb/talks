include image.env

docker-image:
	docker build -t ${IMAGE_NAME}:${IMAGE_TAG} -f Dockerfile .

delete-repo:
	aws ecr-public delete-repository \
		--repository-name ${IMAGE_NAME}

ecr-details.json:
	aws ecr-public create-repository \
		--repository-name ${IMAGE_NAME} \
		> ecr-details.json

create-repo: ecr-details.json

# https://docs.amazonaws.cn/en_us/AmazonECR/latest/public/docker-push-ecr-image.html
push-image: create-repo
	aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
	docker tag
	docker push ${PUBLIC_IMAGE}

start-notebook:
	docker run \
		-v $$(pwd):/root/testing
		-p 9000:8888 \
		-p 8787:8787 \
		--name ${CONTAINER_NAME} \
		${PUBLIC_IMAGE}

stop-notebook:
	@docker kill ${CONTAINER_NAME}
	@docker rm ${CONTAINER_NAME}
