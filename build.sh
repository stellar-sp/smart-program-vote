#!/bin/bash

if [ -z "$1" ]
  then
    echo "No argument supplied, please pass 1 or 2 or ... for image tag"
    exit
fi

export IMAGE_NAME=mlkbenjamin/smart-program-vote:$1

docker build . --no-cache -t $IMAGE_NAME
docker push $IMAGE_NAME
