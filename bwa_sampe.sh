#!/bin/bash
#SBATCH -t 8:00:00
#SBATCH -n 32
#SBATCH -J bwa_aln_Thalassiosira_antarctica_sampe
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com
module load bwa/0.7.12 
bwa sampe /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira-antarctica-CCMP982.cds.fa /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira_antarctica_AB013_forward_paired.sai /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira_antarctica_AB013_reverse_paired.sai /users/jlw578/scratch/reads/AB013_forward_paired.fq /users/jlw578/scratch/reads/AB013_reverse_paired.fq > /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira_antarctica_AB013_bwa_aln.sam
bwa sampe /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira-antarctica-CCMP982.cds.fa /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira_antarctica_AB014_forward_paired.sai /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira_antarctica_AB014_reverse_paired.sai /users/jlw578/scratch/reads/AB014_forward_paired.fq /users/jlw578/scratch/reads/AB014_reverse_paired.fq > /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira_antarctica_AB014_bwa_aln.sam
bwa sampe /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira-antarctica-CCMP982.cds.fa /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira_antarctica_AB015_forward_paired.sai /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira_antarctica_AB015_reverse_paired.sai /users/jlw578/scratch/reads/AB015_forward_paired.fq /users/jlw578/scratch/reads/AB015_reverse_paired.fq > /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira_antarctica_AB015_bwa_aln.sam
