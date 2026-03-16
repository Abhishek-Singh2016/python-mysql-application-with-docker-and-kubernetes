#!/bin/bash

# Build image using the dockerfile present in the folder.
docker build -f dockerfile -t image_mov_app_python .
docker build -t $ECR_REGISTRY/$REPO:Python-mysql-app-$TAG dockerfile
docker push $ECR_REGISTRY/$REPO:Python-mysql-app-$TAG

# Load the image to the Minikube cluster.
#minikube image load image_mov_app_python:latest
docker image list