#!/bin/zsh
cat ../hightemp.txt | cut -f1 | sort | uniq -c | sort -k1 -n -r
