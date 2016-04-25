#!/bin/zsh
cat ../hightemp.txt | cut -f1 | sort | uniq
