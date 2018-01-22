#!/bin/bash
for file in *.fart; do
awk 'BEGIN {FS="\t"} {print $2, $18}' "$file" > "shart_$file"
done
