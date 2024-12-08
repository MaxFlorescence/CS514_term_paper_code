#!/bin/bash

CONT_NAME="${1,,}_container"
CONT_TAG="${1,,}_tag"

echo "Running './collect-all.sh $1 $2 $3 $4'..."
docker build --tag=$CONT_TAG .
docker run --cpus=1 --name=$CONT_NAME $CONT_TAG $1 $2 $3 $4
docker cp "${CONT_NAME}:/home/user/BugsInPy/temp/out" "./out_$4/${CONT_NAME}/"
docker rm $CONT_NAME
