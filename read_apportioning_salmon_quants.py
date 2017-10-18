#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:32:10 2017

@author: joselynn
"""

import pandas as pd

Attheya_septentionalis_ab013=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Attheya_septentionalis_ab013/quant.sf', sep='\t')
Attheya_septentionalis_ab014=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Attheya_septentionalis_ab014/quant.sf', sep='\t')
Attheya_septentionalis_ab015=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Attheya_septentionalis_ab015/quant.sf', sep='\t')

#sum read counts & add to a new column
Attheya_septentionalis_ab013['NumReads_sum']=Attheya_septentionalis_ab013['NumReads'].sum()
#convert reads to reads per million
Attheya_septentionalis_ab013['NumReads_sum_per_million']=Attheya_septentionalis_ab013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Attheya_septentionalis_ab013['NumReads_per_million']=Attheya_septentionalis_ab013['NumReads']/Attheya_septentionalis_ab013['NumReads_sum_per_million']
#sum read counts & add to a new column
Attheya_septentionalis_ab014['NumReads_sum']=Attheya_septentionalis_ab014['NumReads'].sum()
#convert reads to reads per million
Attheya_septentionalis_ab014['NumReads_sum_per_million']=Attheya_septentionalis_ab014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Attheya_septentionalis_ab014['NumReads_per_million']=Attheya_septentionalis_ab014['NumReads']/Attheya_septentionalis_ab014['NumReads_sum_per_million']
#sum read counts & add to a new column
Attheya_septentionalis_ab015['NumReads_sum']=Attheya_septentionalis_ab015['NumReads'].sum()
#convert reads to reads per million
Attheya_septentionalis_ab015['NumReads_sum_per_million']=Attheya_septentionalis_ab015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Attheya_septentionalis_ab015['NumReads_per_million']=Attheya_septentionalis_ab015['NumReads']/Attheya_septentionalis_ab015['NumReads_sum_per_million']
#print the outputs
Attheya_septentionalis_ab013.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Attheya_septentionalis_ab013.txt', sep='\t', index=False)
Attheya_septentionalis_ab014.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Attheya_septentionalis_ab014.txt', sep='\t', index=False)
Attheya_septentionalis_ab015.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Attheya_septentionalis_ab015.txt', sep='\t', index=False)

##########################################################################################

Chaetoceros_neogracile_ab013=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Chaetoceros_neogracile_ab013/quant.sf', sep='\t')
Chaetoceros_neogracile_ab014=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Chaetoceros_neogracile_ab014/quant.sf', sep='\t')
Chaetoceros_neogracile_ab015=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Chaetoceros_neogracile_ab015/quant.sf', sep='\t')

#sum read counts & add to a new column
Chaetoceros_neogracile_ab013['NumReads_sum']=Chaetoceros_neogracile_ab013['NumReads'].sum()
#convert reads to reads per million
Chaetoceros_neogracile_ab013['NumReads_sum_per_million']=Chaetoceros_neogracile_ab013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Chaetoceros_neogracile_ab013['NumReads_per_million']=Chaetoceros_neogracile_ab013['NumReads']/Chaetoceros_neogracile_ab013['NumReads_sum_per_million']
#sum read counts & add to a new column
Chaetoceros_neogracile_ab014['NumReads_sum']=Chaetoceros_neogracile_ab014['NumReads'].sum()
#convert reads to reads per million
Chaetoceros_neogracile_ab014['NumReads_sum_per_million']=Chaetoceros_neogracile_ab014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Chaetoceros_neogracile_ab014['NumReads_per_million']=Chaetoceros_neogracile_ab014['NumReads']/Chaetoceros_neogracile_ab014['NumReads_sum_per_million']
#sum read counts & add to a new column
Chaetoceros_neogracile_ab015['NumReads_sum']=Chaetoceros_neogracile_ab015['NumReads'].sum()
#convert reads to reads per million
Chaetoceros_neogracile_ab015['NumReads_sum_per_million']=Chaetoceros_neogracile_ab015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Chaetoceros_neogracile_ab015['NumReads_per_million']=Chaetoceros_neogracile_ab015['NumReads']/Chaetoceros_neogracile_ab015['NumReads_sum_per_million']
#print the outputs
Chaetoceros_neogracile_ab013.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Chaetoceros_neogracile_ab013.txt', sep='\t', index=False)
Chaetoceros_neogracile_ab014.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Chaetoceros_neogracile_ab014.txt', sep='\t', index=False)
Chaetoceros_neogracile_ab015.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Chaetoceros_neogracile_ab015.txt', sep='\t', index=False)


##########################################################################################



Detonula_confervacea_ab013=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Detonula_confervacea_ab013/quant.sf', sep='\t')
Detonula_confervacea_ab014=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Detonula_confervacea_ab014/quant.sf', sep='\t')
Detonula_confervacea_ab015=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Detonula_confervacea_ab015/quant.sf', sep='\t')

#sum read counts & add to a new column
Detonula_confervacea_ab013['NumReads_sum']=Detonula_confervacea_ab013['NumReads'].sum()
#convert reads to reads per million
Detonula_confervacea_ab013['NumReads_sum_per_million']=Detonula_confervacea_ab013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Detonula_confervacea_ab013['NumReads_per_million']=Detonula_confervacea_ab013['NumReads']/Detonula_confervacea_ab013['NumReads_sum_per_million']
#sum read counts & add to a new column
Detonula_confervacea_ab014['NumReads_sum']=Detonula_confervacea_ab014['NumReads'].sum()
#convert reads to reads per million
Detonula_confervacea_ab014['NumReads_sum_per_million']=Detonula_confervacea_ab014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Detonula_confervacea_ab014['NumReads_per_million']=Detonula_confervacea_ab014['NumReads']/Detonula_confervacea_ab014['NumReads_sum_per_million']
#sum read counts & add to a new column
Detonula_confervacea_ab015['NumReads_sum']=Detonula_confervacea_ab015['NumReads'].sum()
#convert reads to reads per million
Detonula_confervacea_ab015['NumReads_sum_per_million']=Detonula_confervacea_ab015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Detonula_confervacea_ab015['NumReads_per_million']=Detonula_confervacea_ab015['NumReads']/Detonula_confervacea_ab015['NumReads_sum_per_million']
#print the outputs
Detonula_confervacea_ab013.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Detonula_confervacea_ab013.txt', sep='\t', index=False)
Detonula_confervacea_ab014.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Detonula_confervacea_ab014.txt', sep='\t', index=False)
Detonula_confervacea_ab015.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Detonula_confervacea_ab015.txt', sep='\t', index=False)


##########################################################################################

Skeletonema_costatum_ab013=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Skeletonema_costatum_ab013/quant.sf', sep='\t')
Skeletonema_costatum_ab014=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Skeletonema_costatum_ab014/quant.sf', sep='\t')
Skeletonema_costatum_ab015=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Skeletonema_costatum_ab015/quant.sf', sep='\t')

#sum read counts & add to a new column
Skeletonema_costatum_ab013['NumReads_sum']=Skeletonema_costatum_ab013['NumReads'].sum()
#convert reads to reads per million
Skeletonema_costatum_ab013['NumReads_sum_per_million']=Skeletonema_costatum_ab013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_costatum_ab013['NumReads_per_million']=Skeletonema_costatum_ab013['NumReads']/Skeletonema_costatum_ab013['NumReads_sum_per_million']
#sum read counts & add to a new column
Skeletonema_costatum_ab014['NumReads_sum']=Skeletonema_costatum_ab014['NumReads'].sum()
#convert reads to reads per million
Skeletonema_costatum_ab014['NumReads_sum_per_million']=Skeletonema_costatum_ab014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_costatum_ab014['NumReads_per_million']=Skeletonema_costatum_ab014['NumReads']/Skeletonema_costatum_ab014['NumReads_sum_per_million']
#sum read counts & add to a new column
Skeletonema_costatum_ab015['NumReads_sum']=Skeletonema_costatum_ab015['NumReads'].sum()
#convert reads to reads per million
Skeletonema_costatum_ab015['NumReads_sum_per_million']=Skeletonema_costatum_ab015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_costatum_ab015['NumReads_per_million']=Skeletonema_costatum_ab015['NumReads']/Skeletonema_costatum_ab015['NumReads_sum_per_million']
#print the outputs
Skeletonema_costatum_ab013.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Skeletonema_costatum_ab013.txt', sep='\t', index=False)
Skeletonema_costatum_ab014.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Skeletonema_costatum_ab014.txt', sep='\t', index=False)
Skeletonema_costatum_ab015.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Skeletonema_costatum_ab015.txt', sep='\t', index=False)


##########################################################################################


Skeletonema_marinoi_ab013=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Skeletonema_marinoi_ab013/quant.sf', sep='\t')
Skeletonema_marinoi_ab014=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Skeletonema_marinoi_ab014/quant.sf', sep='\t')
Skeletonema_marinoi_ab015=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Skeletonema_marinoi_ab015/quant.sf', sep='\t')

#sum read counts & add to a new column
Skeletonema_marinoi_ab013['NumReads_sum']=Skeletonema_marinoi_ab013['NumReads'].sum()
#convert reads to reads per million
Skeletonema_marinoi_ab013['NumReads_sum_per_million']=Skeletonema_marinoi_ab013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_marinoi_ab013['NumReads_per_million']=Skeletonema_marinoi_ab013['NumReads']/Skeletonema_marinoi_ab013['NumReads_sum_per_million']
#sum read counts & add to a new column
Skeletonema_marinoi_ab014['NumReads_sum']=Skeletonema_marinoi_ab014['NumReads'].sum()
#convert reads to reads per million
Skeletonema_marinoi_ab014['NumReads_sum_per_million']=Skeletonema_marinoi_ab014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_marinoi_ab014['NumReads_per_million']=Skeletonema_marinoi_ab014['NumReads']/Skeletonema_marinoi_ab014['NumReads_sum_per_million']
#sum read counts & add to a new column
Skeletonema_marinoi_ab015['NumReads_sum']=Skeletonema_marinoi_ab015['NumReads'].sum()
#convert reads to reads per million
Skeletonema_marinoi_ab015['NumReads_sum_per_million']=Skeletonema_marinoi_ab015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_marinoi_ab015['NumReads_per_million']=Skeletonema_marinoi_ab015['NumReads']/Skeletonema_marinoi_ab015['NumReads_sum_per_million']
#print the outputs
Skeletonema_marinoi_ab013.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Skeletonema_marinoi_ab013.txt', sep='\t', index=False)
Skeletonema_marinoi_ab014.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Skeletonema_marinoi_ab014.txt', sep='\t', index=False)
Skeletonema_marinoi_ab015.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Skeletonema_marinoi_ab015.txt', sep='\t', index=False)


##########################################################################################


Thalassiosira_antarctica_ab013=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_antarctica_ab013/quant.sf', sep='\t')
Thalassiosira_antarctica_ab014=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_antarctica_ab014/quant.sf', sep='\t')
Thalassiosira_antarctica_ab015=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_antarctica_ab015/quant.sf', sep='\t')

#sum read counts & add to a new column
Thalassiosira_antarctica_ab013['NumReads_sum']=Thalassiosira_antarctica_ab013['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_antarctica_ab013['NumReads_sum_per_million']=Thalassiosira_antarctica_ab013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_antarctica_ab013['NumReads_per_million']=Thalassiosira_antarctica_ab013['NumReads']/Thalassiosira_antarctica_ab013['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_antarctica_ab014['NumReads_sum']=Thalassiosira_antarctica_ab014['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_antarctica_ab014['NumReads_sum_per_million']=Thalassiosira_antarctica_ab014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_antarctica_ab014['NumReads_per_million']=Thalassiosira_antarctica_ab014['NumReads']/Thalassiosira_antarctica_ab014['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_antarctica_ab015['NumReads_sum']=Thalassiosira_antarctica_ab015['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_antarctica_ab015['NumReads_sum_per_million']=Thalassiosira_antarctica_ab015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_antarctica_ab015['NumReads_per_million']=Thalassiosira_antarctica_ab015['NumReads']/Thalassiosira_antarctica_ab015['NumReads_sum_per_million']
#print the outputs
Thalassiosira_antarctica_ab013.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_antarctica_ab013.txt', sep='\t', index=False)
Thalassiosira_antarctica_ab014.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_antarctica_ab014.txt', sep='\t', index=False)
Thalassiosira_antarctica_ab015.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_antarctica_ab015.txt', sep='\t', index=False)


##########################################################################################



Thalassiosira_miniscula_ab013=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_miniscula_ab013/quant.sf', sep='\t')
Thalassiosira_miniscula_ab014=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_miniscula_ab014/quant.sf', sep='\t')
Thalassiosira_miniscula_ab015=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_miniscula_ab015/quant.sf', sep='\t')

#sum read counts & add to a new column
Thalassiosira_miniscula_ab013['NumReads_sum']=Thalassiosira_miniscula_ab013['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_miniscula_ab013['NumReads_sum_per_million']=Thalassiosira_miniscula_ab013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_miniscula_ab013['NumReads_per_million']=Thalassiosira_miniscula_ab013['NumReads']/Thalassiosira_miniscula_ab013['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_miniscula_ab014['NumReads_sum']=Thalassiosira_miniscula_ab014['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_miniscula_ab014['NumReads_sum_per_million']=Thalassiosira_miniscula_ab014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_miniscula_ab014['NumReads_per_million']=Thalassiosira_miniscula_ab014['NumReads']/Thalassiosira_miniscula_ab014['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_miniscula_ab015['NumReads_sum']=Thalassiosira_miniscula_ab015['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_miniscula_ab015['NumReads_sum_per_million']=Thalassiosira_miniscula_ab015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_miniscula_ab015['NumReads_per_million']=Thalassiosira_miniscula_ab015['NumReads']/Thalassiosira_miniscula_ab015['NumReads_sum_per_million']
#print the outputs
Thalassiosira_miniscula_ab013.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_miniscula_ab013.txt', sep='\t', index=False)
Thalassiosira_miniscula_ab014.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_miniscula_ab014.txt', sep='\t', index=False)
Thalassiosira_miniscula_ab015.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_miniscula_ab015.txt', sep='\t', index=False)


##########################################################################################


Thalassiosira_punctigera_ab013=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_punctigera_ab013/quant.sf', sep='\t')
Thalassiosira_punctigera_ab014=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_punctigera_ab014/quant.sf', sep='\t')
Thalassiosira_punctigera_ab015=pd.read_table('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_punctigera_ab015/quant.sf', sep='\t')

#sum read counts & add to a new column
Thalassiosira_punctigera_ab013['NumReads_sum']=Thalassiosira_punctigera_ab013['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_punctigera_ab013['NumReads_sum_per_million']=Thalassiosira_punctigera_ab013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_punctigera_ab013['NumReads_per_million']=Thalassiosira_punctigera_ab013['NumReads']/Thalassiosira_punctigera_ab013['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_punctigera_ab014['NumReads_sum']=Thalassiosira_punctigera_ab014['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_punctigera_ab014['NumReads_sum_per_million']=Thalassiosira_punctigera_ab014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_punctigera_ab014['NumReads_per_million']=Thalassiosira_punctigera_ab014['NumReads']/Thalassiosira_punctigera_ab014['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_punctigera_ab015['NumReads_sum']=Thalassiosira_punctigera_ab015['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_punctigera_ab015['NumReads_sum_per_million']=Thalassiosira_punctigera_ab015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_punctigera_ab015['NumReads_per_million']=Thalassiosira_punctigera_ab015['NumReads']/Thalassiosira_punctigera_ab015['NumReads_sum_per_million']
#print the outputs
Thalassiosira_punctigera_ab013.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_punctigera_ab013.txt', sep='\t', index=False)
Thalassiosira_punctigera_ab014.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_punctigera_ab014.txt', sep='\t', index=False)
Thalassiosira_punctigera_ab015.to_csv('/Users/joselynn/Dropbox/CO2_metatranscriptome/rerun_salmon_20170929/quant/quants/Thalassiosira_punctigera_ab015.txt', sep='\t', index=False)

