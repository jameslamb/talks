# cloud-intro

## Description

> In this presentation, you'll get a light introduction to the public cloud. You'll learn concepts like infrastructure-as-code, high availability, and serverless. You'll see a real-world example of how the public cloud makes it easy to conduct analyses that don't work well on your local machine. This will be a highly interactive demo, where attendees are encouraged to interrupt the presenter and ask questions.

## Where this talk has been given:

* (virtual) University of Illinois, Urbana-Champaign, [IRisk Lab](https://math.illinois.edu/illinois-risk-lab/home) Virtual Workshop series, April 2020

## Agenda

The talk is structured as follows

* [Cloud Concepts](./CLOUD-CONCEPTS.md)
* [Training a model on your laptop](./TRAIN-LOCAL.md)
* [Serving a model on your laptop](./SCORE-LOCAL.md)
* [Training a model with cloud services](./TRAIN-CLOUD.md)
* [Serving a model with cloud services](./SCORE-CLOUD.md)
* [How to learn more](./LEARN-CLOUD.md)
* Question & Answer

## Set up conda env

```shell
conda create \
    --name ticket_closure \
    python=3.7

source activate ticket_closure
```

Create jupyter kernel

```shell
conda install \
    -y \
    nb_conda_kernels

source activate ${CONDA_ENV_NAME}

python -m ipykernel install \
    --user \
    --name ${CONDA_ENV_NAME} \
    --display-name "Python (${CONDA_ENV_NAME})"
```

## Serverless Scoring

```shell
AWS_REGION='us-east-1'
SAM_CODE_BUCKET="sam-files-ed508549-d39c-42ca-940c-d744c1b31299"

# training
aws --region ${AWS_REGION} \
    cloudformation deploy \
        --stack-name 'ticket-closure-training-infra' \
        --template-file training.yml \
        --capabilities "CAPABILITY_AUTO_EXPAND" "CAPABILITY_NAMED_IAM" \
        --no-fail-on-empty-changeset

# scoring
TRAINING_BUCKET=$(
    aws --region ${AWS_REGION} \
        cloudformation describe-stacks \
            --stack-name 'ticket-closure-training-infra' \
            --query "Stacks[0].Outputs[?OutputKey=='oTrainingArtifactsBucketName'].OutputValue" \
            --output text
)

aws --region ${AWS_REGION} \
    cloudformation package \
        --template-file scoring.yml \
        --s3-bucket ${SAM_CODE_BUCKET} \
        --output-template-file sam-scoring.yml

aws --region ${AWS_REGION} \
    cloudformation deploy \
        --stack-name 'ticket-closure-scoring-infra' \
        --template-file sam-scoring.yml \
        --capabilities "CAPABILITY_AUTO_EXPAND" "CAPABILITY_NAMED_IAM" \
        --no-fail-on-empty-changeset \
        --parameter-overrides \
            pTrainingArtifactBucketName=${TRAINING_BUCKET} \
            pScoringArtifactFileKey="model.pkl"
```
