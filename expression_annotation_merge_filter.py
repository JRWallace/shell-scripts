#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:43:07 2017

@author: Joselynn
"""

import pandas as pd
import os
os.chdir("/Users/Joselynn/Dropbox/CO2_metatranscriptome/")

Attheya_septentionalis=pd.read_table('Attheya_septentionalis_2tpm_filtered.txt', sep='\t')
Attheya_septentionalis_ab013_ab014=pd.read_table('Attheya_septentionalis_all_2tpm_filtered_ab013_ab014_postpD', sep='\t')
Attheya_septentionalis_ab014_ab015=pd.read_table('Attheya_septentionalis_all_2tpm_filtered_ab014_ab015_postpD', sep='\t')
id_conversion=pd.read_table('all_ids_tabbed_trimmed.txt', sep='\t', low_memory=False)
annot_data=pd.read_table('query.ko', sep='\t', low_memory=False)
kegg_data=pd.read_table('kegg_ko_filled.txt', sep='\t', low_memory=False)
Attheya_septentionalis_subset=Attheya_septentionalis[['Name','EffectiveLength_ab013', 'NumReads_per_million_ab013', 'NumReads_per_million_ab014', 'NumReads_per_million_ab015']]
Attheya_septentionalis_subset.columns=['orf_id','EffectiveLength_ab013', 'NumReads_per_million_ab013', 'NumReads_per_million_ab014', 'NumReads_per_million_ab015']
Attheya_septentionalis_ab013_ab014.reset_index(level=0, inplace=True)
Attheya_septentionalis_ab014_ab015.reset_index(level=0, inplace=True)
Attheya_septentionalis_ab013_ab014.columns=['orf_id', 'delta_ab013_ab014', 'P(X1/X2>2)_ab013_ab014', 'P(X2/X1>2)_ab013_ab014']
Attheya_septentionalis_ab014_ab015.columns=['orf_id', 'delta_ab014_ab015', 'P(X1/X2>2)_ab014_ab015', 'P(X2/X1>2)_ab014_ab015']
id_conversion.columns=['campep','orf_id']
annot_data.columns=['campep','ko']
Attheya_septentionalis_merge1=Attheya_septentionalis_subset.merge(Attheya_septentionalis_ab013_ab014, how='inner', on='orf_id')
Attheya_septentionalis_merge2=Attheya_septentionalis_merge1.merge(Attheya_septentionalis_ab014_ab015, how='inner', on='orf_id')
Attheya_septentionalis_merge3=Attheya_septentionalis_merge2.merge(id_conversion, how='inner', on='orf_id')
Attheya_septentionalis_merge4=Attheya_septentionalis_merge3.merge(annot_data, how='left', on='campep')
Attheya_septentionalis_merge5=Attheya_septentionalis_merge4.merge(kegg_data, how='left', on='ko')
Attheya_septentionalis_merge5.to_csv('Attheya_septentionalis_everything_pluskaas.txt', sep='\t')
#obviously these columns will change based on what order you ran ASC, manually check the output of the previous file before filtering...
Attheya_septentionalis_up_in_low=Attheya_septentionalis_merge5[(Attheya_septentionalis_merge5['P(X1/X2>2)_ab013_ab014']>=.95)]
Attheya_septentionalis_down_in_low=Attheya_septentionalis_merge5[(Attheya_septentionalis_merge5['P(X2/X1>2)_ab013_ab014']>=.95)]
Attheya_septentionalis_up_in_high=Attheya_septentionalis_merge5[(Attheya_septentionalis_merge5['P(X2/X1>2)_ab014_ab015']>=.95)]
Attheya_septentionalis_down_in_high=Attheya_septentionalis_merge5[(Attheya_septentionalis_merge5['P(X1/X2>2)_ab014_ab015']>=.95)]
Attheya_septentionalis_up_in_low.to_csv('Attheya_septentionalis_up_in_low.txt', sep='\t', index=False)
Attheya_septentionalis_down_in_low.to_csv('Attheya_septentionalis_down_in_low.txt', sep='\t', index=False)
Attheya_septentionalis_up_in_high.to_csv('Attheya_septentionalis_up_in_high.txt', sep='\t', index=False)
Attheya_septentionalis_down_in_high.to_csv('Attheya_septentionalis_down_in_high.txt', sep='\t', index=False)
