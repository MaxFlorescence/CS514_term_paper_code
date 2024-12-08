#!/bin/bash

algorithm="$1"
out_dir="out_${algorithm}_tests"
mkdir -p $out_dir
csv_file="$out_dir/faults_detected.csv"
echo "algorithm,project,bug,detected,check_tests" > $csv_file

for p in $(ls projects); do
	project=${p,,}
	
	for b in $(ls projects/$p/bugs); do
		possible=""
		faults="?"
		
		diffs=$(grep diff projects/$p/bugs/$b/bug_patch.txt | sed -nE 's|^.*/(.+\.py)$|test_\1|p')
		for d in $diffs; do
			look_in="out_$algorithm/${p}_container/all_tests"
			if [ -f "$look_in/$d" ]; then
				echo "Y $p $b $d"
				possible="$possible $d"
			elif [ -f "$look_in/${d,,}" ]; then
				echo "Y $p $b ${d,,}"
				possible="$possible ${d,,}"
			else
				echo "N $p $b $d"
			fi
		done
		
		if [[ $possible == "" ]]; then
			faults=0
		fi
		
		echo "${algorithm},${project},${b},${faults},\"${possible}\"" >> $csv_file
	done
done