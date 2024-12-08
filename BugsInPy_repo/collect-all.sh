#!/bin/bash

ALGORITHM="MIO" # "MIO" "DYNAMOSA" "WHOLE_SUITE"

declare -a projects=("cookiecutter" "fastapi" "httpie" "luigi" "PySnooper" "spacy" "black" "keras" "matplotlib" "scrapy" "thefuck" "tornado" "tqdm" "youtube-dl")
declare -a bugids=(4 16 5 33 3 10 23 45 30 35 32 16 9 43)
declare -a tops=("cookiecutter" "fastapi" "httpie" "luigi" "pysnooper" "spacy" "." "keras" "lib" "scrapy" "thefuck" "tornado" "tqdm" "youtube_dl")

START=13
END=$(( ${#projects[@]} - 1 ))

for I in $(seq $START $END); do
	project=${projects[$I]}
	bugid=${bugids[$I]}
	top=${tops[$I]}
	
	echo "Running ./collect.sh $project $bugid $top..."
	./collect.sh $project $bugid $top $ALGORITHM
	
	sleep 5
	
	cd "out_$ALGORITHM"
	CONTAINER="${project,,}_container/"
	echo "Running ./out_$ALGORITHM/collect_results.sh $CONTAINER $ALGORITHM..."
	./collect_results.sh $CONTAINER $ALGORITHM
	cd ../
	
	sleep 5
done