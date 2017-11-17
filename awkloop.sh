#!/bin/bash
for file in *_blastout.txt; do
awk '{print $2}' "$file" > "ids_$file"
done
