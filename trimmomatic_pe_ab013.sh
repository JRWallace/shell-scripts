#!/bin/bash
#SBATCH -t 1:00:00
#SBATCH -n 32
#SBATCH -J ab013_pe_trimmomatic
#SBATCH --mem=64GB
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com

module load trimmomatic/0.32

java -jar $TRIMMOMATIC_BASE/Trimmomatic-0.32/trimmomatic-0.32.jar PE -threads 16  \
/users/jlw578/data/reads/AB013_GTGAAA_L008_R1_001.fastq.gz AB013_GTGAAA_L008_R2_001.fastq  \/users/jlw578/data/reads/AB013_forward_paired.fq /users/jlw578/data/reads/AB013_forward_singletons.fq /users/jlw578/data/reads/AB013_reverse_paired.fq /users/jlw578/data/reads/AB013_reverse_singletons.fq \
HEADCROP:15 \
SLIDINGWINDOW:6:20 \
MINLEN:25
