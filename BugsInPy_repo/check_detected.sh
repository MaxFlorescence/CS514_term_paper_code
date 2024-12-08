#!/bin/bash

cd $1
for detfile in $(ls *_detected.txt); do
	bug=${detfile%_*}
	tail "${bug}_0.txt" -n 4
	echo
	tail "${bug}_1.txt" -n 4
	echo
	read -p "Detected?: " detected
	sed -ri "s|^(.+),[01],$|\1,$detected,|" $detfile
	cat $detfile
	echo
done
