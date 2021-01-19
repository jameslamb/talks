include image.env

docker-image:
	docker build --no-cache -t ${IMAGE_NAME}:${IMAGE_TAG} -f Dockerfile .

cluster-image:
	docker build --no-cache -t ${CLUSTER_IMAGE_NAME}:${IMAGE_TAG} -f Dockerfile-cluster .

delete-repo:
	aws --region us-east-1 \
		ecr-public batch-delete-image \
			--repository-name ${CLUSTER_IMAGE_NAME} \
			--image-ids imageTag=${IMAGE_TAG}
	aws --region us-east-1 \
		ecr-public delete-repository \
			--repository-name ${CLUSTER_IMAGE_NAME}
	rm ecr-details.json

ecr-details.json:
	aws --region us-east-1 ecr-public create-repository \
		--repository-name ${CLUSTER_IMAGE_NAME} \
		> ecr-details.json

create-repo: ecr-details.json

# https://docs.amazonaws.cn/en_us/AmazonECR/latest/public/docker-push-ecr-image.html
push-image: create-repo
	aws --region us-east-1 ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws
	docker tag ${CLUSTER_IMAGE_NAME}:${IMAGE_TAG} $$(cat ecr-details.json | jq .'repository'.'repositoryUri' | tr -d '"'):1
	docker push $$(cat ecr-details.json | jq .'repository'.'repositoryUri' | tr -d '"'):1

start-notebook:
	docker run \
		-v $$(pwd):/home/jovyan/testing \
		--env AWS_SECRET_ACCESS_KEY=$${AWS_SECRET_ACCESS_KEY:-notset} \
		--env AWS_ACCESS_KEY_ID=$${AWS_ACCESS_KEY_ID:-notset} \
		-p 8888:8888 \
		-p 8787:8787 \
		--name ${CONTAINER_NAME} \
		${IMAGE_NAME}:${IMAGE_TAG}

stop-notebook:
	@docker kill ${CONTAINER_NAME}
	@docker rm ${CONTAINER_NAME}
