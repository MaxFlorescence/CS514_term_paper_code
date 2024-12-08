#!/bin/bash

declare -a projects=("black" "cookiecutter" "fastapi" "httpie" "keras" "luigi" "matplotlib" "pandas" "sanic" "scrapy" "spacy" "thefuck" "tornado" "tqdm" "youtube-dl")

for project in "${projects[@]}"; do
	echo "==========$project=========="
	docker compose up setup $project-dates --build > commit-dates/$project.txt
	rm projects/bugsinpy-index.csv
	rm -rf temp/projects/*
	docker compose down
done
