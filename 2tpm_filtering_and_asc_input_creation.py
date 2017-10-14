#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 18:22:48 2017

@author: joselynn
"""

import pandas as pd

Attheya_septentionalis_ab013=pd.read_table('Attheya_septentionalis_ab013.txt', sep='\t', low_memory=False)
Attheya_septentionalis_ab013.columns=['Name','Length_ab013','EffectiveLength_ab013','TPM_ab013','NumReads_ab013','NumReads_sum_ab013','NumReads_sum_per_million_ab013','NumReads_per_million_ab013']
Attheya_septentionalis_ab014=pd.read_table('Attheya_septentionalis_ab014.txt', sep='\t', low_memory=False)
Attheya_septentionalis_ab014.columns=['Name','Length_ab014','EffectiveLength_ab014','TPM_ab014','NumReads_ab014','NumReads_sum_ab014','NumReads_sum_per_million_ab014','NumReads_per_million_ab014']
Attheya_septentionalis_ab015=pd.read_table('Attheya_septentionalis_ab015.txt', sep='\t', low_memory=False)
Attheya_septentionalis_ab015.columns=['Name','Length_ab015','EffectiveLength_ab015','TPM_ab015','NumReads_ab015','NumReads_sum_ab015','NumReads_sum_per_million_ab015','NumReads_per_million_ab015']
Attheya_septentionalis_ab013_ab014=Attheya_septentionalis_ab013.merge(Attheya_septentionalis_ab014, how='inner', on='Name')
Attheya_septentionalis_all=Attheya_septentionalis_ab013_ab014.merge(Attheya_septentionalis_ab015, how='inner', on='Name')
Attheya_septentionalis_all_2tpm_filtered=Attheya_septentionalis_all[(Attheya_septentionalis_all['TPM_ab013']>=2)|(Attheya_septentionalis_all['TPM_ab014']>=2)|(Attheya_septentionalis_all['TPM_ab015']>=2)]
Attheya_septentionalis_all_2tpm_filtered.to_csv('Attheya_septentionalis_2tpm_filtered.txt', sep='\t', index=False)
Attheya_septentionalis_all_2tpm_filtered_ids=Attheya_septentionalis_all_2tpm_filtered.loc[:,'Name']
Attheya_septentionalis_all_2tpm_filtered_ids.to_csv('Attheya_septentionalis_all_2tpm_filtered_ids.txt', sep='\t', index=False)
Attheya_septentionalis_all_2tpm_filtered_ab013_cpm=Attheya_septentionalis_all_2tpm_filtered.loc[:,'NumReads_per_million_ab013']
Attheya_septentionalis_all_2tpm_filtered_ab013_cpm.to_csv('Attheya_septentionalis_all_2tpm_filtered_ab013_cpm.txt', sep='\t', index=False)
Attheya_septentionalis_all_2tpm_filtered_ab014_cpm=Attheya_septentionalis_all_2tpm_filtered.loc[:,'NumReads_per_million_ab014']
Attheya_septentionalis_all_2tpm_filtered_ab014_cpm.to_csv('Attheya_septentionalis_all_2tpm_filtered_ab014_cpm.txt', sep='\t', index=False)
Attheya_septentionalis_all_2tpm_filtered_ab015_cpm=Attheya_septentionalis_all_2tpm_filtered.loc[:,'NumReads_per_million_ab015']
Attheya_septentionalis_all_2tpm_filtered_ab015_cpm.to_csv('Attheya_septentionalis_all_2tpm_filtered_ab015_cpm.txt', sep='\t', index=False)
##########################################################################################
Chaetoceros_neogracile_ab013=pd.read_table('Chaetoceros_neogracile_ab013.txt', sep='\t', low_memory=False)
Chaetoceros_neogracile_ab013.columns=['Name','Length_ab013','EffectiveLength_ab013','TPM_ab013','NumReads_ab013','NumReads_sum_ab013','NumReads_sum_per_million_ab013','NumReads_per_million_ab013']
Chaetoceros_neogracile_ab014=pd.read_table('Chaetoceros_neogracile_ab014.txt', sep='\t', low_memory=False)
Chaetoceros_neogracile_ab014.columns=['Name','Length_ab014','EffectiveLength_ab014','TPM_ab014','NumReads_ab014','NumReads_sum_ab014','NumReads_sum_per_million_ab014','NumReads_per_million_ab014']
Chaetoceros_neogracile_ab015=pd.read_table('Chaetoceros_neogracile_ab015.txt', sep='\t', low_memory=False)
Chaetoceros_neogracile_ab015.columns=['Name','Length_ab015','EffectiveLength_ab015','TPM_ab015','NumReads_ab015','NumReads_sum_ab015','NumReads_sum_per_million_ab015','NumReads_per_million_ab015']
Chaetoceros_neogracile_ab013_ab014=Chaetoceros_neogracile_ab013.merge(Chaetoceros_neogracile_ab014, how='inner', on='Name')
Chaetoceros_neogracile_all=Chaetoceros_neogracile_ab013_ab014.merge(Chaetoceros_neogracile_ab015, how='inner', on='Name')
Chaetoceros_neogracile_all_2tpm_filtered=Chaetoceros_neogracile_all[(Chaetoceros_neogracile_all['TPM_ab013']>=2)|(Chaetoceros_neogracile_all['TPM_ab014']>=2)|(Chaetoceros_neogracile_all['TPM_ab015']>=2)]
Chaetoceros_neogracile_all_2tpm_filtered.to_csv('Chaetoceros_neogracile_2tpm_filtered.txt', sep='\t', index=False)
Chaetoceros_neogracile_all_2tpm_filtered_ids=Chaetoceros_neogracile_all_2tpm_filtered.loc[:,'Name']
Chaetoceros_neogracile_all_2tpm_filtered_ids.to_csv('Chaetoceros_neogracile_all_2tpm_filtered_ids.txt', sep='\t', index=False)
Chaetoceros_neogracile_all_2tpm_filtered_ab013_cpm=Chaetoceros_neogracile_all_2tpm_filtered.loc[:,'NumReads_per_million_ab013']
Chaetoceros_neogracile_all_2tpm_filtered_ab013_cpm.to_csv('Chaetoceros_neogracile_all_2tpm_filtered_ab013_cpm.txt', sep='\t', index=False)
Chaetoceros_neogracile_all_2tpm_filtered_ab014_cpm=Chaetoceros_neogracile_all_2tpm_filtered.loc[:,'NumReads_per_million_ab014']
Chaetoceros_neogracile_all_2tpm_filtered_ab014_cpm.to_csv('Chaetoceros_neogracile_all_2tpm_filtered_ab014_cpm.txt', sep='\t', index=False)
Chaetoceros_neogracile_all_2tpm_filtered_ab015_cpm=Chaetoceros_neogracile_all_2tpm_filtered.loc[:,'NumReads_per_million_ab015']
Chaetoceros_neogracile_all_2tpm_filtered_ab015_cpm.to_csv('Chaetoceros_neogracile_all_2tpm_filtered_ab015_cpm.txt', sep='\t', index=False)
##########################################################################################
Detonula_confervacea_ab013=pd.read_table('Detonula_confervacea_ab013.txt', sep='\t', low_memory=False)
Detonula_confervacea_ab013.columns=['Name','Length_ab013','EffectiveLength_ab013','TPM_ab013','NumReads_ab013','NumReads_sum_ab013','NumReads_sum_per_million_ab013','NumReads_per_million_ab013']
Detonula_confervacea_ab014=pd.read_table('Detonula_confervacea_ab014.txt', sep='\t', low_memory=False)
Detonula_confervacea_ab014.columns=['Name','Length_ab014','EffectiveLength_ab014','TPM_ab014','NumReads_ab014','NumReads_sum_ab014','NumReads_sum_per_million_ab014','NumReads_per_million_ab014']
Detonula_confervacea_ab015=pd.read_table('Detonula_confervacea_ab015.txt', sep='\t', low_memory=False)
Detonula_confervacea_ab015.columns=['Name','Length_ab015','EffectiveLength_ab015','TPM_ab015','NumReads_ab015','NumReads_sum_ab015','NumReads_sum_per_million_ab015','NumReads_per_million_ab015']
Detonula_confervacea_ab013_ab014=Detonula_confervacea_ab013.merge(Detonula_confervacea_ab014, how='inner', on='Name')
Detonula_confervacea_all=Detonula_confervacea_ab013_ab014.merge(Detonula_confervacea_ab015, how='inner', on='Name')
Detonula_confervacea_all_2tpm_filtered=Detonula_confervacea_all[(Detonula_confervacea_all['TPM_ab013']>=2)|(Detonula_confervacea_all['TPM_ab014']>=2)|(Detonula_confervacea_all['TPM_ab015']>=2)]
Detonula_confervacea_all_2tpm_filtered.to_csv('Detonula_confervacea_2tpm_filtered.txt', sep='\t', index=False)
Detonula_confervacea_all_2tpm_filtered_ids=Detonula_confervacea_all_2tpm_filtered.loc[:,'Name']
Detonula_confervacea_all_2tpm_filtered_ids.to_csv('Detonula_confervacea_all_2tpm_filtered_ids.txt', sep='\t', index=False)
Detonula_confervacea_all_2tpm_filtered_ab013_cpm=Detonula_confervacea_all_2tpm_filtered.loc[:,'NumReads_per_million_ab013']
Detonula_confervacea_all_2tpm_filtered_ab013_cpm.to_csv('Detonula_confervacea_all_2tpm_filtered_ab013_cpm.txt', sep='\t', index=False)
Detonula_confervacea_all_2tpm_filtered_ab014_cpm=Detonula_confervacea_all_2tpm_filtered.loc[:,'NumReads_per_million_ab014']
Detonula_confervacea_all_2tpm_filtered_ab014_cpm.to_csv('Detonula_confervacea_all_2tpm_filtered_ab014_cpm.txt', sep='\t', index=False)
Detonula_confervacea_all_2tpm_filtered_ab015_cpm=Detonula_confervacea_all_2tpm_filtered.loc[:,'NumReads_per_million_ab015']
Detonula_confervacea_all_2tpm_filtered_ab015_cpm.to_csv('Detonula_confervacea_all_2tpm_filtered_ab015_cpm.txt', sep='\t', index=False)
##########################################################################################
Skeletonema_costatum_ab013=pd.read_table('Skeletonema_costatum_ab013.txt', sep='\t', low_memory=False)
Skeletonema_costatum_ab013.columns=['Name','Length_ab013','EffectiveLength_ab013','TPM_ab013','NumReads_ab013','NumReads_sum_ab013','NumReads_sum_per_million_ab013','NumReads_per_million_ab013']
Skeletonema_costatum_ab014=pd.read_table('Skeletonema_costatum_ab014.txt', sep='\t', low_memory=False)
Skeletonema_costatum_ab014.columns=['Name','Length_ab014','EffectiveLength_ab014','TPM_ab014','NumReads_ab014','NumReads_sum_ab014','NumReads_sum_per_million_ab014','NumReads_per_million_ab014']
Skeletonema_costatum_ab015=pd.read_table('Skeletonema_costatum_ab015.txt', sep='\t', low_memory=False)
Skeletonema_costatum_ab015.columns=['Name','Length_ab015','EffectiveLength_ab015','TPM_ab015','NumReads_ab015','NumReads_sum_ab015','NumReads_sum_per_million_ab015','NumReads_per_million_ab015']
Skeletonema_costatum_ab013_ab014=Skeletonema_costatum_ab013.merge(Skeletonema_costatum_ab014, how='inner', on='Name')
Skeletonema_costatum_all=Skeletonema_costatum_ab013_ab014.merge(Skeletonema_costatum_ab015, how='inner', on='Name')
Skeletonema_costatum_all_2tpm_filtered=Skeletonema_costatum_all[(Skeletonema_costatum_all['TPM_ab013']>=2)|(Skeletonema_costatum_all['TPM_ab014']>=2)|(Skeletonema_costatum_all['TPM_ab015']>=2)]
Skeletonema_costatum_all_2tpm_filtered.to_csv('Skeletonema_costatum_2tpm_filtered.txt', sep='\t', index=False)
Skeletonema_costatum_all_2tpm_filtered_ids=Skeletonema_costatum_all_2tpm_filtered.loc[:,'Name']
Skeletonema_costatum_all_2tpm_filtered_ids.to_csv('Skeletonema_costatum_all_2tpm_filtered_ids.txt', sep='\t', index=False)
Skeletonema_costatum_all_2tpm_filtered_ab013_cpm=Skeletonema_costatum_all_2tpm_filtered.loc[:,'NumReads_per_million_ab013']
Skeletonema_costatum_all_2tpm_filtered_ab013_cpm.to_csv('Skeletonema_costatum_all_2tpm_filtered_ab013_cpm.txt', sep='\t', index=False)
Skeletonema_costatum_all_2tpm_filtered_ab014_cpm=Skeletonema_costatum_all_2tpm_filtered.loc[:,'NumReads_per_million_ab014']
Skeletonema_costatum_all_2tpm_filtered_ab014_cpm.to_csv('Skeletonema_costatum_all_2tpm_filtered_ab014_cpm.txt', sep='\t', index=False)
Skeletonema_costatum_all_2tpm_filtered_ab015_cpm=Skeletonema_costatum_all_2tpm_filtered.loc[:,'NumReads_per_million_ab015']
Skeletonema_costatum_all_2tpm_filtered_ab015_cpm.to_csv('Skeletonema_costatum_all_2tpm_filtered_ab015_cpm.txt', sep='\t', index=False)
##########################################################################################
Skeletonema_marinoi_ab013=pd.read_table('Skeletonema_marinoi_ab013.txt', sep='\t', low_memory=False)
Skeletonema_marinoi_ab013.columns=['Name','Length_ab013','EffectiveLength_ab013','TPM_ab013','NumReads_ab013','NumReads_sum_ab013','NumReads_sum_per_million_ab013','NumReads_per_million_ab013']
Skeletonema_marinoi_ab014=pd.read_table('Skeletonema_marinoi_ab014.txt', sep='\t', low_memory=False)
Skeletonema_marinoi_ab014.columns=['Name','Length_ab014','EffectiveLength_ab014','TPM_ab014','NumReads_ab014','NumReads_sum_ab014','NumReads_sum_per_million_ab014','NumReads_per_million_ab014']
Skeletonema_marinoi_ab015=pd.read_table('Skeletonema_marinoi_ab015.txt', sep='\t', low_memory=False)
Skeletonema_marinoi_ab015.columns=['Name','Length_ab015','EffectiveLength_ab015','TPM_ab015','NumReads_ab015','NumReads_sum_ab015','NumReads_sum_per_million_ab015','NumReads_per_million_ab015']
Skeletonema_marinoi_ab013_ab014=Skeletonema_marinoi_ab013.merge(Skeletonema_marinoi_ab014, how='inner', on='Name')
Skeletonema_marinoi_all=Skeletonema_marinoi_ab013_ab014.merge(Skeletonema_marinoi_ab015, how='inner', on='Name')
Skeletonema_marinoi_all_2tpm_filtered=Skeletonema_marinoi_all[(Skeletonema_marinoi_all['TPM_ab013']>=2)|(Skeletonema_marinoi_all['TPM_ab014']>=2)|(Skeletonema_marinoi_all['TPM_ab015']>=2)]
Skeletonema_marinoi_all_2tpm_filtered.to_csv('Skeletonema_marinoi_2tpm_filtered.txt', sep='\t', index=False)
Skeletonema_marinoi_all_2tpm_filtered_ids=Skeletonema_marinoi_all_2tpm_filtered.loc[:,'Name']
Skeletonema_marinoi_all_2tpm_filtered_ids.to_csv('Skeletonema_marinoi_all_2tpm_filtered_ids.txt', sep='\t', index=False)
Skeletonema_marinoi_all_2tpm_filtered_ab013_cpm=Skeletonema_marinoi_all_2tpm_filtered.loc[:,'NumReads_per_million_ab013']
Skeletonema_marinoi_all_2tpm_filtered_ab013_cpm.to_csv('Skeletonema_marinoi_all_2tpm_filtered_ab013_cpm.txt', sep='\t', index=False)
Skeletonema_marinoi_all_2tpm_filtered_ab014_cpm=Skeletonema_marinoi_all_2tpm_filtered.loc[:,'NumReads_per_million_ab014']
Skeletonema_marinoi_all_2tpm_filtered_ab014_cpm.to_csv('Skeletonema_marinoi_all_2tpm_filtered_ab014_cpm.txt', sep='\t', index=False)
Skeletonema_marinoi_all_2tpm_filtered_ab015_cpm=Skeletonema_marinoi_all_2tpm_filtered.loc[:,'NumReads_per_million_ab015']
Skeletonema_marinoi_all_2tpm_filtered_ab015_cpm.to_csv('Skeletonema_marinoi_all_2tpm_filtered_ab015_cpm.txt', sep='\t', index=False)
##########################################################################################
Thalassiosira_antarctica_ab013=pd.read_table('Thalassiosira_antarctica_ab013.txt', sep='\t', low_memory=False)
Thalassiosira_antarctica_ab013.columns=['Name','Length_ab013','EffectiveLength_ab013','TPM_ab013','NumReads_ab013','NumReads_sum_ab013','NumReads_sum_per_million_ab013','NumReads_per_million_ab013']
Thalassiosira_antarctica_ab014=pd.read_table('Thalassiosira_antarctica_ab014.txt', sep='\t', low_memory=False)
Thalassiosira_antarctica_ab014.columns=['Name','Length_ab014','EffectiveLength_ab014','TPM_ab014','NumReads_ab014','NumReads_sum_ab014','NumReads_sum_per_million_ab014','NumReads_per_million_ab014']
Thalassiosira_antarctica_ab015=pd.read_table('Thalassiosira_antarctica_ab015.txt', sep='\t', low_memory=False)
Thalassiosira_antarctica_ab015.columns=['Name','Length_ab015','EffectiveLength_ab015','TPM_ab015','NumReads_ab015','NumReads_sum_ab015','NumReads_sum_per_million_ab015','NumReads_per_million_ab015']
Thalassiosira_antarctica_ab013_ab014=Thalassiosira_antarctica_ab013.merge(Thalassiosira_antarctica_ab014, how='inner', on='Name')
Thalassiosira_antarctica_all=Thalassiosira_antarctica_ab013_ab014.merge(Thalassiosira_antarctica_ab015, how='inner', on='Name')
Thalassiosira_antarctica_all_2tpm_filtered=Thalassiosira_antarctica_all[(Thalassiosira_antarctica_all['TPM_ab013']>=2)|(Thalassiosira_antarctica_all['TPM_ab014']>=2)|(Thalassiosira_antarctica_all['TPM_ab015']>=2)]
Thalassiosira_antarctica_all_2tpm_filtered.to_csv('Thalassiosira_antarctica_2tpm_filtered.txt', sep='\t', index=False)
Thalassiosira_antarctica_all_2tpm_filtered_ids=Thalassiosira_antarctica_all_2tpm_filtered.loc[:,'Name']
Thalassiosira_antarctica_all_2tpm_filtered_ids.to_csv('Thalassiosira_antarctica_all_2tpm_filtered_ids.txt', sep='\t', index=False)
Thalassiosira_antarctica_all_2tpm_filtered_ab013_cpm=Thalassiosira_antarctica_all_2tpm_filtered.loc[:,'NumReads_per_million_ab013']
Thalassiosira_antarctica_all_2tpm_filtered_ab013_cpm.to_csv('Thalassiosira_antarctica_all_2tpm_filtered_ab013_cpm.txt', sep='\t', index=False)
Thalassiosira_antarctica_all_2tpm_filtered_ab014_cpm=Thalassiosira_antarctica_all_2tpm_filtered.loc[:,'NumReads_per_million_ab014']
Thalassiosira_antarctica_all_2tpm_filtered_ab014_cpm.to_csv('Thalassiosira_antarctica_all_2tpm_filtered_ab014_cpm.txt', sep='\t', index=False)
Thalassiosira_antarctica_all_2tpm_filtered_ab015_cpm=Thalassiosira_antarctica_all_2tpm_filtered.loc[:,'NumReads_per_million_ab015']
Thalassiosira_antarctica_all_2tpm_filtered_ab015_cpm.to_csv('Thalassiosira_antarctica_all_2tpm_filtered_ab015_cpm.txt', sep='\t', index=False)
##########################################################################################
Thalassiosira_punctigera_ab013=pd.read_table('Thalassiosira_punctigera_ab013.txt', sep='\t', low_memory=False)
Thalassiosira_punctigera_ab013.columns=['Name','Length_ab013','EffectiveLength_ab013','TPM_ab013','NumReads_ab013','NumReads_sum_ab013','NumReads_sum_per_million_ab013','NumReads_per_million_ab013']
Thalassiosira_punctigera_ab014=pd.read_table('Thalassiosira_punctigera_ab014.txt', sep='\t', low_memory=False)
Thalassiosira_punctigera_ab014.columns=['Name','Length_ab014','EffectiveLength_ab014','TPM_ab014','NumReads_ab014','NumReads_sum_ab014','NumReads_sum_per_million_ab014','NumReads_per_million_ab014']
Thalassiosira_punctigera_ab015=pd.read_table('Thalassiosira_punctigera_ab015.txt', sep='\t', low_memory=False)
Thalassiosira_punctigera_ab015.columns=['Name','Length_ab015','EffectiveLength_ab015','TPM_ab015','NumReads_ab015','NumReads_sum_ab015','NumReads_sum_per_million_ab015','NumReads_per_million_ab015']
Thalassiosira_punctigera_ab013_ab014=Thalassiosira_punctigera_ab013.merge(Thalassiosira_punctigera_ab014, how='inner', on='Name')
Thalassiosira_punctigera_all=Thalassiosira_punctigera_ab013_ab014.merge(Thalassiosira_punctigera_ab015, how='inner', on='Name')
Thalassiosira_punctigera_all_2tpm_filtered=Thalassiosira_punctigera_all[(Thalassiosira_punctigera_all['TPM_ab013']>=2)|(Thalassiosira_punctigera_all['TPM_ab014']>=2)|(Thalassiosira_punctigera_all['TPM_ab015']>=2)]
Thalassiosira_punctigera_all_2tpm_filtered.to_csv('Thalassiosira_punctigera_2tpm_filtered.txt', sep='\t', index=False)
Thalassiosira_punctigera_all_2tpm_filtered_ids=Thalassiosira_punctigera_all_2tpm_filtered.loc[:,'Name']
Thalassiosira_punctigera_all_2tpm_filtered_ids.to_csv('Thalassiosira_punctigera_all_2tpm_filtered_ids.txt', sep='\t', index=False)
Thalassiosira_punctigera_all_2tpm_filtered_ab013_cpm=Thalassiosira_punctigera_all_2tpm_filtered.loc[:,'NumReads_per_million_ab013']
Thalassiosira_punctigera_all_2tpm_filtered_ab013_cpm.to_csv('Thalassiosira_punctigera_all_2tpm_filtered_ab013_cpm.txt', sep='\t', index=False)
Thalassiosira_punctigera_all_2tpm_filtered_ab014_cpm=Thalassiosira_punctigera_all_2tpm_filtered.loc[:,'NumReads_per_million_ab014']
Thalassiosira_punctigera_all_2tpm_filtered_ab014_cpm.to_csv('Thalassiosira_punctigera_all_2tpm_filtered_ab014_cpm.txt', sep='\t', index=False)
Thalassiosira_punctigera_all_2tpm_filtered_ab015_cpm=Thalassiosira_punctigera_all_2tpm_filtered.loc[:,'NumReads_per_million_ab015']
Thalassiosira_punctigera_all_2tpm_filtered_ab015_cpm.to_csv('Thalassiosira_punctigera_all_2tpm_filtered_ab015_cpm.txt', sep='\t', index=False)
##########################################################################################
Thalassiosira_miniscula_ab013=pd.read_table('Thalassiosira_miniscula_ab013.txt', sep='\t', low_memory=False)
Thalassiosira_miniscula_ab013.columns=['Name','Length_ab013','EffectiveLength_ab013','TPM_ab013','NumReads_ab013','NumReads_sum_ab013','NumReads_sum_per_million_ab013','NumReads_per_million_ab013']
Thalassiosira_miniscula_ab014=pd.read_table('Thalassiosira_miniscula_ab014.txt', sep='\t', low_memory=False)
Thalassiosira_miniscula_ab014.columns=['Name','Length_ab014','EffectiveLength_ab014','TPM_ab014','NumReads_ab014','NumReads_sum_ab014','NumReads_sum_per_million_ab014','NumReads_per_million_ab014']
Thalassiosira_miniscula_ab015=pd.read_table('Thalassiosira_miniscula_ab015.txt', sep='\t', low_memory=False)
Thalassiosira_miniscula_ab015.columns=['Name','Length_ab015','EffectiveLength_ab015','TPM_ab015','NumReads_ab015','NumReads_sum_ab015','NumReads_sum_per_million_ab015','NumReads_per_million_ab015']
Thalassiosira_miniscula_ab013_ab014=Thalassiosira_miniscula_ab013.merge(Thalassiosira_miniscula_ab014, how='inner', on='Name')
Thalassiosira_miniscula_all=Thalassiosira_miniscula_ab013_ab014.merge(Thalassiosira_miniscula_ab015, how='inner', on='Name')
Thalassiosira_miniscula_all_2tpm_filtered=Thalassiosira_miniscula_all[(Thalassiosira_miniscula_all['TPM_ab013']>=2)|(Thalassiosira_miniscula_all['TPM_ab014']>=2)|(Thalassiosira_miniscula_all['TPM_ab015']>=2)]
Thalassiosira_miniscula_all_2tpm_filtered.to_csv('Thalassiosira_miniscula_2tpm_filtered.txt', sep='\t', index=False)
Thalassiosira_miniscula_all_2tpm_filtered_ids=Thalassiosira_miniscula_all_2tpm_filtered.loc[:,'Name']
Thalassiosira_miniscula_all_2tpm_filtered_ids.to_csv('Thalassiosira_miniscula_all_2tpm_filtered_ids.txt', sep='\t', index=False)
Thalassiosira_miniscula_all_2tpm_filtered_ab013_cpm=Thalassiosira_miniscula_all_2tpm_filtered.loc[:,'NumReads_per_million_ab013']
Thalassiosira_miniscula_all_2tpm_filtered_ab013_cpm.to_csv('Thalassiosira_miniscula_all_2tpm_filtered_ab013_cpm.txt', sep='\t', index=False)
Thalassiosira_miniscula_all_2tpm_filtered_ab014_cpm=Thalassiosira_miniscula_all_2tpm_filtered.loc[:,'NumReads_per_million_ab014']
Thalassiosira_miniscula_all_2tpm_filtered_ab014_cpm.to_csv('Thalassiosira_miniscula_all_2tpm_filtered_ab014_cpm.txt', sep='\t', index=False)
Thalassiosira_miniscula_all_2tpm_filtered_ab015_cpm=Thalassiosira_miniscula_all_2tpm_filtered.loc[:,'NumReads_per_million_ab015']
Thalassiosira_miniscula_all_2tpm_filtered_ab015_cpm.to_csv('Thalassiosira_miniscula_all_2tpm_filtered_ab015_cpm.txt', sep='\t', index=False)