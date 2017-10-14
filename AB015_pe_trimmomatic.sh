#!/bin/bash
#SBATCH -t 8:00:00
#SBATCH -n 32
#SBATCH -J ab015_pe_trimmomatic
#SBATCH --mem=64GB
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com
module load trimmomatic/0.32

java -jar $TRIMMOMATIC_BASE/Trimmomatic-0.32/trimmomatic-0.32.jar PE -threads 32  \
/users/jlw578/scratch/reads/AB015_GTTTCG_L008_R1_001.fastq.bz2 /users/jlw578/scratch/reads/AB015_GTTTCG_L008_R2_001.fastq.bz2 \
/users/jlw578/scratch/reads/pe_trim/AB015_forward_paired.fq /users/jlw578/scratch/reads/pe_trim/AB015_forward_singletons.fq /users/jlw578/scratch/reads/pe_trim/AB015_reverse_paired.fq /users/jlw578/scratch/reads/pe_trim/AB015_reverse_singletons.fq \
ILLUMINACLIP:/users/jlw578/scratch/reads/trimmomatic_provided_truseq_adapters.fa:2:30:10 \
HEADCROP:15 \
SLIDINGWINDOW:6:20 \
MINLEN:25

