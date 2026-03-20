#!/bin/bash

# Build image using the dockerfile present in the folder.
#docker build -f dockerfile -t image_mov_app_python .

docker build -f dockerfile -t $ECR_REGISTRY/$REPO:Python-mysql-app-$TAG .
docker push $ECR_REGISTRY/$REPO:Python-mysql-app-$TAG
#ERROR: failed to build: invalid tag "702175642104.dkr.ecr.us-east-1.amazonaws.com/:mysql-db-": invalid reference format

#Deployment
#kubectl apply -f ../python-app-deployment.yaml
#kubectl apply -f ../python-app-service.yaml

# Load the image to the Minikube cluster.
#minikube image load image_mov_app_python:latest
#docker image list