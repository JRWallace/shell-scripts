#!/bin/bash
#SBATCH -t 8:00:00
#SBATCH --mem=16g
#SBATCH -c 32
#SBATCH -J uniqu_ab015_reverse
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com

awk '{ print $1 }' AB015_reverse_paired_out | sort | uniq -u > AB015_reverse_paired_out_uniqu

fgrep -f AB015_reverse_paired_out_uniqu AB015_reverse_paired_out > AB015_reverse_paired_out_uniqu_full_line

awk '{ print $2 }' AB015_reverse_paired_out_uniqu_full_line > AB015_reverse_paired_out_uniqu_campep_ids

