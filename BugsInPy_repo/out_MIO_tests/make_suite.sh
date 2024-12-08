#!/bin/bash

for D in $(ls -d */); do
    if [[ "$D" == *"_container/" ]]; then
        echo "Making suite for ${D%/}..."
        cd ${D%/}
		TOP=$(cat topdir.txt)
        rm -r all_tests
        mkdir all_tests
		echo "" > "all_tests/__init__.py"
        for R in $(ls -d report_*/); do
            REPORT=${R%%/}
            SUITE=$(echo $REPORT | sed -nE 's/report_(.+)/suite_\1/p')
            FILE=$(ls $REPORT/$SUITE/*.py | sed -nE 's|.+/(.+\.py)|\1|p')
            cp "$REPORT/$SUITE/$FILE" ./all_tests/

            # fix import
			#sedstring="s/pynguin log (.+).py/\1/;s|/|.|g;s/^\.+/$TOP./;s/^\.+//p"
            #sed -iE "s/import .* as module_0/import $IMPORTPATH as module_0/" "all_tests/$FILE"
            #IMPORTPATH=$(head $REPORT/log.txt -n 1 | sed -nE "$sedstring")
        done
        cd ../
    fi
done