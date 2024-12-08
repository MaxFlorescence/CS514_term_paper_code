#!/bin/bash

get_top () {
  if [[ "$1" == "PySnooper" ]]; then
	echo "pysnooper"
  elif [[ "$1" == "black" ]]; then
	echo "."
  elif [[ "$1" == "matplotlib" ]]; then
	echo "lib"
  elif [[ "$1" == "youtube-dl" ]]; then
	echo "youtube_dl"
  else
	echo "$1"
  fi
}

for line in $(cat CHECK_THESE.csv); do
	IFS=, read -r alg proj bug det file <<< $line
	if [[ "$proj" == "project" ]]; then continue; fi
	top=$(get_top $proj)
	
	./collect_tests.sh $proj $bug $alg $top $file
	
	sleep 10
done