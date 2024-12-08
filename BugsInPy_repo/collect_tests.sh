#!/bin/bash

if [ "$#" -ne 5 ]; then
	echo "usage: ./collect_tests.sh [proj] [bug] [alg] [top] [file]"
	exit 1
else
	read -r proj bug alg top file <<< $@
fi

CONT_NAME="${proj,,}_container"
CONT_TAG="${proj,,}_tag"

echo "Running \"./collect_tests.sh $proj $bug $alg $top $file\"..."
docker build --tag=$CONT_TAG .
docker run --cpus=1 --name=$CONT_NAME $CONT_TAG $proj $bug $alg $top $file
docker cp "${CONT_NAME}:/home/user/BugsInPy/temp/test_out/." "./out_${alg}_tests/${CONT_NAME}/"
docker rm $CONT_NAME
