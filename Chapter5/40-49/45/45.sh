#!/bin/zsh
cat output.txt | sort | uniq -c | sort -nr > ranking.txt

function get_pattern() {
    echo "^$1\t"
    cat output.txt | grep "^$1\t" | sort | uniq -c | sort -nr > pattern_$1.txt
}

words=("する" "見る" "与える")
for i in "${words[@]}"; do
    get_pattern $i
done

