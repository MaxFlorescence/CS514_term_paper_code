#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: ./collect_results.sh [dir] [algorithm]"
	exit 1
fi

# filter out bad modules
COUNT=$(ls $1 | wc -l)
COUNT=$(( ($COUNT-1)/2 - 1 ))
echo "$(($COUNT+1)) total modules"

cd $1
mkdir bad
BAD_COUNT=0
for I in $(seq 0 $COUNT); do
	SUITE=$(ls "suite_$I" | wc -l)
	
	if [[ $SUITE -eq 0 ]]; then
		mv "suite_$I" bad/
		mv "report_$I" bad/
		BAD_COUNT=$(($BAD_COUNT+1))
	else
		mv "suite_$I" "report_$I/"
	fi
done

# collect data for good modules
OUT="$2_stats1.csv"
echo "Module,Coverage,TestCount,GeneratedMutants,SurvivingMutants" > $OUT
for REPORT in $(ls | grep report); do
	cd $REPORT
	
	TEST_COUNT=$(cat suite_*/*.py | grep "def test_" | wc -l)
	if [[ $TEST_COUNT -eq 0 ]]; then
		BAD_COUNT=$(($BAD_COUNT+1))
		continue
	fi

    GEN_MUTANTS=$(sed -nE 's/^.+Generated ([0-9]+) mutants.+$/\1/p' log.txt)
    SUR_MUTANTS=$(sed -nE 's/^.+Number of Surviving Mutant\(s\): ([0-9]+).+$/\1/p' log.txt)
	
	LINE=$(cat statistics.csv | tail -n 1)
	echo $LINE,\"$TEST_COUNT\",\"$GEN_MUTANTS\",\"$SUR_MUTANTS\" >> ../$OUT
	
	cd ../
done

echo "$BAD_COUNT bad modules"