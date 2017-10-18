#!/bin/bash
for file in ids_*
do
	cat "$file" | sort | uniq | wc -l > "ids_counts$file"
done
