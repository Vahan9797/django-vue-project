#!/usr/bin/env bash

# Check if no argument is passed so there is a need to install all dependencies...
mainFile=./requirements.txt

if [ $# -eq 0 ]; then
	pip install $(cat $mainFile | xargs)
else
	for arg in "$@"; do
		if [ $1 = '--dev' ]; then
			mainFile=./requirements-dev.txt
			continue
		else
			pip install "$arg"
		fi
	done
fi

truncate -s 0 $mainFile
pip freeze >> $mainFile