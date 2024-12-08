#!/bin/bash

if [ "$#" -eq 0 ]; then
    echo "Usage: pynguin-script.sh [algorithm] [skip-files...]"
	exit 1
else
	ALGORITHM="$1"
	SKIP=${@:2}
fi

OUT_DIR="/home/user/out_$ALGORITHM"
PROJ_DIR="Summer2023Redistricting"
WORK_DIR="/home/user/$PROJ_DIR"
BUG_ID="0"
TOPLEVEL_DIR="Repartitioning"

# ------------------------------------setup out dir------------------------------------
echo
echo ===================================Setup out dir...===================================
mkdir -p $OUT_DIR
cd $OUT_DIR
echo "Log file" > log.txt
echo $(ls)

# ------------------------------------check environment------------------------------------
echo
echo ===================================Check environment...===================================
#export PYNGUIN_DANGER_AWARE=1
#export PYTHONIOENCODING=utf-8
#check=$(conda info | grep "active environment")
#if [[ "$check" != *"redistricting"* ]]; then
#	echo "wrong conda environment! ($check)"
#	exit 1
#fi
check=$(python --version)
if [[ "$check" != "Python 3.10.14" ]]; then
	echo "wrong python version! ($check)"
	exit 1
fi
check=$(pynguin --version)
if [[ "$check" != "pynguin 0.40.0" ]]; then
	echo "wrong pynguin version! ($check)"
	exit 1
fi

#cd $WORK_DIR
#conda init bash
#source /root/.bashrc

#conda env create -f environment.yml -y
#conda create -n redistricting -c conda-forge -y python=3.10.14 pip ipykernel geopandas networkx mapclassify matplotlib tqdm scipy #numpy ipywidgets
#conda activate redistricting
#pip install gerrychain==0.3.1
#pip install pynguin

# ------------------------------------run pynguin------------------------------------
echo
echo ===================================Run pynguin...===================================
cd $WORK_DIR/$TOPLEVEL_DIR
I=0
echo "skipping files: ${SKIP[@]}"

for FILE in $(find -name "*.py"); do
	FILE_DIR="${FILE%/*}"
	FILE_BASE="${FILE##*/}"
	FILE_NAME="${FILE_BASE%.py}"
	if [[ "$FILE_NAME" == "__init__" || "$FILE" == *"test"* || "$FILE" == *"build"* ]]; then
		continue
	fi
	
	if [[ ${SKIP[@]} =~ $FILE_NAME ]]; then continue; fi
	
	SUITE_DIR="$OUT_DIR/suite_${I}"
	mkdir -p $SUITE_DIR
	REPORT_DIR="$OUT_DIR/report_${I}"
	mkdir -p $REPORT_DIR
	cd $REPORT_DIR
	echo "pynguin log $FILE" > log.txt
	cd $WORK_DIR/$TOPLEVEL_DIR
	
	echo "   Running on module $I ($FILE)..."
	echo "   Running on module $I ($FILE)..." &>> $OUT_DIR/log.txt
	pynguin -v --algorithm=$ALGORITHM --project-path="$WORK_DIR/$TOPLEVEL_DIR/$FILE_DIR" --module-name=$FILE_NAME --output-path=$SUITE_DIR --report-dir=$REPORT_DIR --maximum_search_time=300 --coverage-metrics=BRANCH &>> $REPORT_DIR/log.txt
	#echo PYNGUINCOMMAND &>> $REPORT_DIR/log.txt &
	
	I=$(($I+1))
done

# debug
#pynguin -v --project-path="$WORK_DIR/$TOP_DIR" --module-name="pysnooper" --output-path="$OUT_DIR/suite_$I" --report-dir="$OUT_DIR/report_$I" --maximum_search_time=300 --coverage-metrics=BRANCH --maximum-coverage-plateau 1000 #>> OUT 2>> ERR
