#!/bin/bash

if [[ -r highscore.txt ]]; then
	if [[ -n $1 ]]; then
		echo $1 > highscore.txt 
	fi
	echo | cat highscore.txt
else
	echo 0 > highscore.txt
fi
