#!/bin/bash
#SBATCH -t 48:00:00
#SBATCH -n 16
#SBATCH -J makedb_diamond
#SBATCH --mem=64GB
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com

module load diamond/0.8.37 

diamond makedb --in /users/jlw578/scratch/mmetsp_oneline_files/mmetsp_ids/prot/output/clustered/concatenated_clustered/concatedated_clustered_mmetsp_prots.txt -d /users/jlw578/data/diamond/mmetsp_98_db -p 16

