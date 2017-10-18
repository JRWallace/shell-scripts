#!/bin/bash
#SBATCH -t 8:00:00
#SBATCH -n 32
#SBATCH -J jw_salmon_quant_skeletonema_marinoi
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com
module load salmon/0.10.0
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Skeletonema_marinoi_index -l IU -1 /users/jlw578/scratch/reads/AB013_forward_paired.fq -2 /users/jlw578/scratch/reads/AB013_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Skeletonema_marinoi_ab013 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Skeletonema_marinoi_index -l IU -1 /users/jlw578/scratch/reads/AB014_forward_paired.fq -2 /users/jlw578/scratch/reads/AB014_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Skeletonema_marinoi_ab014 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Skeletonema_marinoi_index -l IU -1 /users/jlw578/scratch/reads/AB015_forward_paired.fq -2 /users/jlw578/scratch/reads/AB015_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Skeletonema_marinoi_ab015 -p 32

salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Skeletonema_costatum_index -l IU -1 /users/jlw578/scratch/reads/AB013_forward_paired.fq -2 /users/jlw578/scratch/reads/AB013_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Skeletonema_costatum_ab013 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Skeletonema_costatum_index -l IU -1 /users/jlw578/scratch/reads/AB014_forward_paired.fq -2 /users/jlw578/scratch/reads/AB014_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Skeletonema_costatum_ab014 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Skeletonema_costatum_index -l IU -1 /users/jlw578/scratch/reads/AB015_forward_paired.fq -2 /users/jlw578/scratch/reads/AB015_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Skeletonema_costatum_ab015 -p 32

salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Thalassiosira_antarctica_index -l IU -1 /users/jlw578/scratch/reads/AB013_forward_paired.fq -2 /users/jlw578/scratch/reads/AB013_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Thalassiosira_antarctica_ab013 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Thalassiosira_antarctica_index -l IU -1 /users/jlw578/scratch/reads/AB014_forward_paired.fq -2 /users/jlw578/scratch/reads/AB014_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Thalassiosira_antarctica_ab014 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Thalassiosira_antarctica_index -l IU -1 /users/jlw578/scratch/reads/AB015_forward_paired.fq -2 /users/jlw578/scratch/reads/AB015_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Thalassiosira_antarctica_ab015 -p 32

salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Thalassiosira_miniscula_index -l IU -1 /users/jlw578/scratch/reads/AB013_forward_paired.fq -2 /users/jlw578/scratch/reads/AB013_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Thalassiosira_miniscula_ab013 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Thalassiosira_miniscula_index -l IU -1 /users/jlw578/scratch/reads/AB014_forward_paired.fq -2 /users/jlw578/scratch/reads/AB014_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Thalassiosira_miniscula_ab014 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Thalassiosira_miniscula_index -l IU -1 /users/jlw578/scratch/reads/AB015_forward_paired.fq -2 /users/jlw578/scratch/reads/AB015_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Thalassiosira_miniscula_ab015 -p 32

salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Thalassiosira_punctigera_index -l IU -1 /users/jlw578/scratch/reads/AB013_forward_paired.fq -2 /users/jlw578/scratch/reads/AB013_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Thalassiosira_punctigera_ab013 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Thalassiosira_punctigera_index -l IU -1 /users/jlw578/scratch/reads/AB014_forward_paired.fq -2 /users/jlw578/scratch/reads/AB014_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Thalassiosira_punctigera_ab014 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Thalassiosira_punctigera_index -l IU -1 /users/jlw578/scratch/reads/AB015_forward_paired.fq -2 /users/jlw578/scratch/reads/AB015_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Thalassiosira_punctigera_ab015 -p 32

salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Detonula_confervacea_index -l IU -1 /users/jlw578/scratch/reads/AB013_forward_paired.fq -2 /users/jlw578/scratch/reads/AB013_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Detonula_confervacea_ab013 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Detonula_confervacea_index -l IU -1 /users/jlw578/scratch/reads/AB014_forward_paired.fq -2 /users/jlw578/scratch/reads/AB014_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Detonula_confervacea_ab014 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Detonula_confervacea_index -l IU -1 /users/jlw578/scratch/reads/AB015_forward_paired.fq -2 /users/jlw578/scratch/reads/AB015_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Detonula_confervacea_ab015 -p 32

salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Attheya_septentionalis_index -l IU -1 /users/jlw578/scratch/reads/AB013_forward_paired.fq -2 /users/jlw578/scratch/reads/AB013_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Attheya_septentionalis_ab013 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Attheya_septentionalis_index -l IU -1 /users/jlw578/scratch/reads/AB014_forward_paired.fq -2 /users/jlw578/scratch/reads/AB014_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Attheya_septentionalis_ab014 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Attheya_septentionalis_index -l IU -1 /users/jlw578/scratch/reads/AB015_forward_paired.fq -2 /users/jlw578/scratch/reads/AB015_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Attheya_septentionalis_ab015 -p 32

salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Chaetoceros_neogracile_index -l IU -1 /users/jlw578/scratch/reads/AB013_forward_paired.fq -2 /users/jlw578/scratch/reads/AB013_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Chaetoceros_neogracile_ab013 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Chaetoceros_neogracile_index -l IU -1 /users/jlw578/scratch/reads/AB014_forward_paired.fq -2 /users/jlw578/scratch/reads/AB014_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Chaetoceros_neogracile_ab014 -p 32
salmon quant -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Chaetoceros_neogracile_index -l IU -1 /users/jlw578/scratch/reads/AB015_forward_paired.fq -2 /users/jlw578/scratch/reads/AB015_reverse_paired.fq -o /users/jlw578/scratch/salmon_september2017_remap/quants/Chaetoceros_neogracile_ab015 -p 32
