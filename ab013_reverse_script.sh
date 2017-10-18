#!/bin/bash
#SBATCH -t 8:00:00
#SBATCH --mem=16g
#SBATCH -c 32
#SBATCH -J uniqu_ab013_reverse
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com

awk '{ print $1 }' AB013_reverse_paired_out | sort | uniq -u > AB013_reverse_paired_out_uniqu

fgrep -f AB013_reverse_paired_out_uniqu AB013_reverse_paired_out > AB013_reverse_paired_out_uniqu_full_line

awk '{ print $2 }' AB013_reverse_paired_out_uniqu_full_line > AB013_reverse_paired_out_uniqu_campep_ids

