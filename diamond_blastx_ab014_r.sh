#!/bin/bash
#SBATCH -t 48:00:00
#SBATCH -n 16
#SBATCH -J ab014_r_diamond
#SBATCH --mem=64GB
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com

module load diamond/0.8.37 

diamond blastx -d /users/jlw578/data/diamond/mmetsp_98_db.dmnd -q /users/jlw578/data/reads/AB014_reverse_paired.fq -o /users/jlw578/data/diamond/noevaluecutoff/top0/AB014_reverse_paired_out -p 16 -f 6 qseqid sseqid sallseqid evalue bitscore score length pident stitle salltitles qcovhsp qtitle --top 0 
