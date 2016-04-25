#!/bin/zsh
cat ../hightemp.txt | wc -l | sed 's,^ *,,; s, *$,,'
