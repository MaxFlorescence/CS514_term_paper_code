#!/bin/bash

# $1: algorithm

CONT_NAME="redistricting_container"
CONT_TAG="redistricting_tag"

docker rm $CONT_NAME
echo "Running './collect.sh $@'..."
docker build --tag=$CONT_TAG .
docker run --cpus=1 --name=$CONT_NAME $CONT_TAG $@
docker cp "${CONT_NAME}:/home/user/out_$1/." "./out_${1}_tests/${CONT_NAME}/"
docker rm $CONT_NAME
