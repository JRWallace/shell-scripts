#!/bin/bash
#SBATCH -t 8:00:00
#SBATCH --mem=16g
#SBATCH -c 32
#SBATCH -J uniqu_ab014_forward
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com

awk '{ print $1 }' AB014_forward_paired_out | sort | uniq -u > AB014_forward_paired_out_uniqu

fgrep -f AB014_forward_paired_out_uniqu AB014_forward_paired_out > AB014_forward_paired_out_uniqu_full_line

awk '{ print $2 }' AB014_forward_paired_out_uniqu_full_line > AB014_forward_paired_out_uniqu_campep_ids

