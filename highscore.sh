#!/bin/bash

if [[ -r highscore.txt ]]; then
	if [[ -n $1 ]]; then
		echo $1 > highscore.txt 
	else
		echo | cat highscore.txt
	fi
else
	echo 0 > highscore.txt
fi
