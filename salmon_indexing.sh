#!/bin/bash
#SBATCH -t 8:00:00
#SBATCH -n 32
#SBATCH -J jw_salmon_index_skeletonema_marinoi
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com
module load salmon/0.10.0
salmon index -t /users/jlw578/scratch/salmon_september2017_remap/Skeletonema_marinoi/Skeletonema_marinoi_all_98 -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Skeletonema_marinoi_index --type quasi -k 31
salmon index -t /users/jlw578/scratch/salmon_september2017_remap/Attheya_septentionalis/MMETSP1449.cds.fa -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Attheya_septentionalis_index --type quasi -k 31
salmon index -t /users/jlw578/scratch/salmon_september2017_remap/Chaetoceros_neogracile/MMETSP1336.cds.fa -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Chaetoceros_neogracile_index --type quasi -k 31
salmon index -t /users/jlw578/scratch/salmon_september2017_remap/Detonula_confervacea/MMETSP1058.cds.fa -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Detonula_confervacea_index --type quasi -k 31
salmon index -t /users/jlw578/scratch/salmon_september2017_remap/Skeletonema_costatum/ MMETSP0013.cds.fa -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Skeletonema_costatum_index --type quasi -k 31
salmon index -t /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_antarctica/Thalassiosira-antarctica-CCMP982.cds.fa -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Thalassiosira_antarctica_index --type quasi -k 31
salmon index -t /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_miniscula/Thalassiosira-miniscula-CCMP1093.cds.fa -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Thalassiosira_miniscula_index --type quasi -k 31
salmon index -t /users/jlw578/scratch/salmon_september2017_remap/Thalassiosira_punctigera/MMETSP1067.cds.fa -i /users/jlw578/scratch/salmon_september2017_remap/indexes/Thalassiosira_punctigera_index --type quasi -k 31
