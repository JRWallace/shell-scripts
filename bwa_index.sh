#!/bin/bash
#SBATCH -t 8:00:00
#SBATCH -n 32
#SBATCH -J bwa_index_Thalassiosira_antarctica
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com
module load bwa/0.7.12 
bwa index /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira-antarctica-CCMP982.cds.fa
