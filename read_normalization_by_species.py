#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:20:12 2018

@author: joselynn
"""
import pandas as pd
##########################################################################################
Skeletonema_costatum_AB013=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_costatum_camnt_salmon_quant_AB013_quant.sf', sep='\t')
Skeletonema_costatum_AB014=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_costatum_camnt_salmon_quant_AB014_quant.sf', sep='\t')
Skeletonema_costatum_AB015=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_costatum_camnt_salmon_quant_AB015_quant.sf', sep='\t')
#sum read counts & add to a new column
Skeletonema_costatum_AB013['NumReads_sum']=Skeletonema_costatum_AB013['NumReads'].sum()
#convert reads to reads per million
Skeletonema_costatum_AB013['NumReads_sum_per_million']=Skeletonema_costatum_AB013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_costatum_AB013['NumReads_per_million']=Skeletonema_costatum_AB013['NumReads']/Skeletonema_costatum_AB013['NumReads_sum_per_million']
#sum read counts & add to a new column
Skeletonema_costatum_AB014['NumReads_sum']=Skeletonema_costatum_AB014['NumReads'].sum()
#convert reads to reads per million
Skeletonema_costatum_AB014['NumReads_sum_per_million']=Skeletonema_costatum_AB014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_costatum_AB014['NumReads_per_million']=Skeletonema_costatum_AB014['NumReads']/Skeletonema_costatum_AB014['NumReads_sum_per_million']
#sum read counts & add to a new column
Skeletonema_costatum_AB015['NumReads_sum']=Skeletonema_costatum_AB015['NumReads'].sum()
#convert reads to reads per million
Skeletonema_costatum_AB015['NumReads_sum_per_million']=Skeletonema_costatum_AB015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_costatum_AB015['NumReads_per_million']=Skeletonema_costatum_AB015['NumReads']/Skeletonema_costatum_AB015['NumReads_sum_per_million']

#round the dfs
Skeletonema_costatum_AB013=Skeletonema_costatum_AB013.round(decimals=0)
Skeletonema_costatum_AB014=Skeletonema_costatum_AB014.round(decimals=0)
Skeletonema_costatum_AB015=Skeletonema_costatum_AB015.round(decimals=0)

#print the outputs
Skeletonema_costatum_AB013.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_costatum_AB013.txt', sep='\t', index=False)
Skeletonema_costatum_AB014.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_costatum_AB014.txt', sep='\t', index=False)
Skeletonema_costatum_AB015.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_costatum_AB015.txt', sep='\t', index=False)
##########################################################################################
Skeletonema_dohrnii_AB013=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_dohrnii_camnt_salmon_quant_AB013_quant.sf', sep='\t')
Skeletonema_dohrnii_AB014=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_dohrnii_camnt_salmon_quant_AB014_quant.sf', sep='\t')
Skeletonema_dohrnii_AB015=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_dohrnii_camnt_salmon_quant_AB015_quant.sf', sep='\t')
#sum read counts & add to a new column
Skeletonema_dohrnii_AB013['NumReads_sum']=Skeletonema_dohrnii_AB013['NumReads'].sum()
#convert reads to reads per million
Skeletonema_dohrnii_AB013['NumReads_sum_per_million']=Skeletonema_dohrnii_AB013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_dohrnii_AB013['NumReads_per_million']=Skeletonema_dohrnii_AB013['NumReads']/Skeletonema_dohrnii_AB013['NumReads_sum_per_million']
#sum read counts & add to a new column
Skeletonema_dohrnii_AB014['NumReads_sum']=Skeletonema_dohrnii_AB014['NumReads'].sum()
#convert reads to reads per million
Skeletonema_dohrnii_AB014['NumReads_sum_per_million']=Skeletonema_dohrnii_AB014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_dohrnii_AB014['NumReads_per_million']=Skeletonema_dohrnii_AB014['NumReads']/Skeletonema_dohrnii_AB014['NumReads_sum_per_million']
#sum read counts & add to a new column
Skeletonema_dohrnii_AB015['NumReads_sum']=Skeletonema_dohrnii_AB015['NumReads'].sum()
#convert reads to reads per million
Skeletonema_dohrnii_AB015['NumReads_sum_per_million']=Skeletonema_dohrnii_AB015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_dohrnii_AB015['NumReads_per_million']=Skeletonema_dohrnii_AB015['NumReads']/Skeletonema_dohrnii_AB015['NumReads_sum_per_million']

#round the dfs
Skeletonema_dohrnii_AB013=Skeletonema_dohrnii_AB013.round(decimals=0)
Skeletonema_dohrnii_AB014=Skeletonema_dohrnii_AB014.round(decimals=0)
Skeletonema_dohrnii_AB015=Skeletonema_dohrnii_AB015.round(decimals=0)

#print the outputs
Skeletonema_dohrnii_AB013.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_dohrnii_AB013.txt', sep='\t', index=False)
Skeletonema_dohrnii_AB014.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_dohrnii_AB014.txt', sep='\t', index=False)
Skeletonema_dohrnii_AB015.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_dohrnii_AB015.txt', sep='\t', index=False)
##########################################################################################
Skeletonema_marinoi_AB013=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_marinoi_camnt_salmon_quant_AB013_quant.sf', sep='\t')
Skeletonema_marinoi_AB014=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_marinoi_camnt_salmon_quant_AB014_quant.sf', sep='\t')
Skeletonema_marinoi_AB015=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_marinoi_camnt_salmon_quant_AB015_quant.sf', sep='\t')
#sum read counts & add to a new column
Skeletonema_marinoi_AB013['NumReads_sum']=Skeletonema_marinoi_AB013['NumReads'].sum()
#convert reads to reads per million
Skeletonema_marinoi_AB013['NumReads_sum_per_million']=Skeletonema_marinoi_AB013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_marinoi_AB013['NumReads_per_million']=Skeletonema_marinoi_AB013['NumReads']/Skeletonema_marinoi_AB013['NumReads_sum_per_million']
#sum read counts & add to a new column
Skeletonema_marinoi_AB014['NumReads_sum']=Skeletonema_marinoi_AB014['NumReads'].sum()
#convert reads to reads per million
Skeletonema_marinoi_AB014['NumReads_sum_per_million']=Skeletonema_marinoi_AB014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_marinoi_AB014['NumReads_per_million']=Skeletonema_marinoi_AB014['NumReads']/Skeletonema_marinoi_AB014['NumReads_sum_per_million']
#sum read counts & add to a new column
Skeletonema_marinoi_AB015['NumReads_sum']=Skeletonema_marinoi_AB015['NumReads'].sum()
#convert reads to reads per million
Skeletonema_marinoi_AB015['NumReads_sum_per_million']=Skeletonema_marinoi_AB015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_marinoi_AB015['NumReads_per_million']=Skeletonema_marinoi_AB015['NumReads']/Skeletonema_marinoi_AB015['NumReads_sum_per_million']

#round the dfs
Skeletonema_marinoi_AB013=Skeletonema_marinoi_AB013.round(decimals=0)
Skeletonema_marinoi_AB014=Skeletonema_marinoi_AB014.round(decimals=0)
Skeletonema_marinoi_AB015=Skeletonema_marinoi_AB015.round(decimals=0)

#print the outputs
Skeletonema_marinoi_AB013.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_marinoi_AB013.txt', sep='\t', index=False)
Skeletonema_marinoi_AB014.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_marinoi_AB014.txt', sep='\t', index=False)
Skeletonema_marinoi_AB015.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_marinoi_AB015.txt', sep='\t', index=False)
##########################################################################################
Skeletonema_menzelii_AB013=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_menzelii_camnt_salmon_quant_AB013_quant.sf', sep='\t')
Skeletonema_menzelii_AB014=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_menzelii_camnt_salmon_quant_AB014_quant.sf', sep='\t')
Skeletonema_menzelii_AB015=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_menzelii_camnt_salmon_quant_AB015_quant.sf', sep='\t')
#sum read counts & add to a new column
Skeletonema_menzelii_AB013['NumReads_sum']=Skeletonema_menzelii_AB013['NumReads'].sum()
#convert reads to reads per million
Skeletonema_menzelii_AB013['NumReads_sum_per_million']=Skeletonema_menzelii_AB013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_menzelii_AB013['NumReads_per_million']=Skeletonema_menzelii_AB013['NumReads']/Skeletonema_menzelii_AB013['NumReads_sum_per_million']
#sum read counts & add to a new column
Skeletonema_menzelii_AB014['NumReads_sum']=Skeletonema_menzelii_AB014['NumReads'].sum()
#convert reads to reads per million
Skeletonema_menzelii_AB014['NumReads_sum_per_million']=Skeletonema_menzelii_AB014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_menzelii_AB014['NumReads_per_million']=Skeletonema_menzelii_AB014['NumReads']/Skeletonema_menzelii_AB014['NumReads_sum_per_million']
#sum read counts & add to a new column
Skeletonema_menzelii_AB015['NumReads_sum']=Skeletonema_menzelii_AB015['NumReads'].sum()
#convert reads to reads per million
Skeletonema_menzelii_AB015['NumReads_sum_per_million']=Skeletonema_menzelii_AB015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Skeletonema_menzelii_AB015['NumReads_per_million']=Skeletonema_menzelii_AB015['NumReads']/Skeletonema_menzelii_AB015['NumReads_sum_per_million']

#round the dfs
Skeletonema_menzelii_AB013=Skeletonema_menzelii_AB013.round(decimals=0)
Skeletonema_menzelii_AB014=Skeletonema_menzelii_AB014.round(decimals=0)
Skeletonema_menzelii_AB015=Skeletonema_menzelii_AB015.round(decimals=0)

#print the outputs
Skeletonema_menzelii_AB013.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_menzelii_AB013.txt', sep='\t', index=False)
Skeletonema_menzelii_AB014.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_menzelii_AB014.txt', sep='\t', index=False)
Skeletonema_menzelii_AB015.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Skeletonema_menzelii_AB015.txt', sep='\t', index=False)
##########################################################################################
Thalassiosira_antarctica_AB013=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_antarctica_camnt_salmon_quant_AB013_quant.sf', sep='\t')
Thalassiosira_antarctica_AB014=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_antarctica_camnt_salmon_quant_AB014_quant.sf', sep='\t')
Thalassiosira_antarctica_AB015=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_antarctica_camnt_salmon_quant_AB015_quant.sf', sep='\t')
#sum read counts & add to a new column
Thalassiosira_antarctica_AB013['NumReads_sum']=Thalassiosira_antarctica_AB013['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_antarctica_AB013['NumReads_sum_per_million']=Thalassiosira_antarctica_AB013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_antarctica_AB013['NumReads_per_million']=Thalassiosira_antarctica_AB013['NumReads']/Thalassiosira_antarctica_AB013['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_antarctica_AB014['NumReads_sum']=Thalassiosira_antarctica_AB014['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_antarctica_AB014['NumReads_sum_per_million']=Thalassiosira_antarctica_AB014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_antarctica_AB014['NumReads_per_million']=Thalassiosira_antarctica_AB014['NumReads']/Thalassiosira_antarctica_AB014['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_antarctica_AB015['NumReads_sum']=Thalassiosira_antarctica_AB015['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_antarctica_AB015['NumReads_sum_per_million']=Thalassiosira_antarctica_AB015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_antarctica_AB015['NumReads_per_million']=Thalassiosira_antarctica_AB015['NumReads']/Thalassiosira_antarctica_AB015['NumReads_sum_per_million']

#round the dfs
Thalassiosira_antarctica_AB013=Thalassiosira_antarctica_AB013.round(decimals=0)
Thalassiosira_antarctica_AB014=Thalassiosira_antarctica_AB014.round(decimals=0)
Thalassiosira_antarctica_AB015=Thalassiosira_antarctica_AB015.round(decimals=0)

#print the outputs
Thalassiosira_antarctica_AB013.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_antarctica_AB013.txt', sep='\t', index=False)
Thalassiosira_antarctica_AB014.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_antarctica_AB014.txt', sep='\t', index=False)
Thalassiosira_antarctica_AB015.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_antarctica_AB015.txt', sep='\t', index=False)
##########################################################################################
Thalassiosira_gravida_AB013=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_gravida_camnt_salmon_quant_AB013_quant.sf', sep='\t')
Thalassiosira_gravida_AB014=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_gravida_camnt_salmon_quant_AB014_quant.sf', sep='\t')
Thalassiosira_gravida_AB015=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_gravida_camnt_salmon_quant_AB015_quant.sf', sep='\t')
#sum read counts & add to a new column
Thalassiosira_gravida_AB013['NumReads_sum']=Thalassiosira_gravida_AB013['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_gravida_AB013['NumReads_sum_per_million']=Thalassiosira_gravida_AB013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_gravida_AB013['NumReads_per_million']=Thalassiosira_gravida_AB013['NumReads']/Thalassiosira_gravida_AB013['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_gravida_AB014['NumReads_sum']=Thalassiosira_gravida_AB014['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_gravida_AB014['NumReads_sum_per_million']=Thalassiosira_gravida_AB014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_gravida_AB014['NumReads_per_million']=Thalassiosira_gravida_AB014['NumReads']/Thalassiosira_gravida_AB014['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_gravida_AB015['NumReads_sum']=Thalassiosira_gravida_AB015['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_gravida_AB015['NumReads_sum_per_million']=Thalassiosira_gravida_AB015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_gravida_AB015['NumReads_per_million']=Thalassiosira_gravida_AB015['NumReads']/Thalassiosira_gravida_AB015['NumReads_sum_per_million']

#round the dfs
Thalassiosira_gravida_AB013=Thalassiosira_gravida_AB013.round(decimals=0)
Thalassiosira_gravida_AB014=Thalassiosira_gravida_AB014.round(decimals=0)
Thalassiosira_gravida_AB015=Thalassiosira_gravida_AB015.round(decimals=0)

#print the outputs
Thalassiosira_gravida_AB013.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_gravida_AB013.txt', sep='\t', index=False)
Thalassiosira_gravida_AB014.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_gravida_AB014.txt', sep='\t', index=False)
Thalassiosira_gravida_AB015.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_gravida_AB015.txt', sep='\t', index=False)
##########################################################################################
Thalassiosira_miniscula_AB013=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_miniscula_camnt_salmon_quant_AB013_quant.sf', sep='\t')
Thalassiosira_miniscula_AB014=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_miniscula_camnt_salmon_quant_AB014_quant.sf', sep='\t')
Thalassiosira_miniscula_AB015=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_miniscula_camnt_salmon_quant_AB015_quant.sf', sep='\t')
#sum read counts & add to a new column
Thalassiosira_miniscula_AB013['NumReads_sum']=Thalassiosira_miniscula_AB013['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_miniscula_AB013['NumReads_sum_per_million']=Thalassiosira_miniscula_AB013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_miniscula_AB013['NumReads_per_million']=Thalassiosira_miniscula_AB013['NumReads']/Thalassiosira_miniscula_AB013['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_miniscula_AB014['NumReads_sum']=Thalassiosira_miniscula_AB014['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_miniscula_AB014['NumReads_sum_per_million']=Thalassiosira_miniscula_AB014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_miniscula_AB014['NumReads_per_million']=Thalassiosira_miniscula_AB014['NumReads']/Thalassiosira_miniscula_AB014['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_miniscula_AB015['NumReads_sum']=Thalassiosira_miniscula_AB015['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_miniscula_AB015['NumReads_sum_per_million']=Thalassiosira_miniscula_AB015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_miniscula_AB015['NumReads_per_million']=Thalassiosira_miniscula_AB015['NumReads']/Thalassiosira_miniscula_AB015['NumReads_sum_per_million']

#round the dfs
Thalassiosira_miniscula_AB013=Thalassiosira_miniscula_AB013.round(decimals=0)
Thalassiosira_miniscula_AB014=Thalassiosira_miniscula_AB014.round(decimals=0)
Thalassiosira_miniscula_AB015=Thalassiosira_miniscula_AB015.round(decimals=0)

#print the outputs
Thalassiosira_miniscula_AB013.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_miniscula_AB013.txt', sep='\t', index=False)
Thalassiosira_miniscula_AB014.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_miniscula_AB014.txt', sep='\t', index=False)
Thalassiosira_miniscula_AB015.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_miniscula_AB015.txt', sep='\t', index=False)
##########################################################################################
Thalassiosira_oceanica_AB013=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_oceanica_camnt_salmon_quant_AB013_quant.sf', sep='\t')
Thalassiosira_oceanica_AB014=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_oceanica_camnt_salmon_quant_AB014_quant.sf', sep='\t')
Thalassiosira_oceanica_AB015=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_oceanica_camnt_salmon_quant_AB015_quant.sf', sep='\t')
#sum read counts & add to a new column
Thalassiosira_oceanica_AB013['NumReads_sum']=Thalassiosira_oceanica_AB013['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_oceanica_AB013['NumReads_sum_per_million']=Thalassiosira_oceanica_AB013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_oceanica_AB013['NumReads_per_million']=Thalassiosira_oceanica_AB013['NumReads']/Thalassiosira_oceanica_AB013['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_oceanica_AB014['NumReads_sum']=Thalassiosira_oceanica_AB014['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_oceanica_AB014['NumReads_sum_per_million']=Thalassiosira_oceanica_AB014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_oceanica_AB014['NumReads_per_million']=Thalassiosira_oceanica_AB014['NumReads']/Thalassiosira_oceanica_AB014['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_oceanica_AB015['NumReads_sum']=Thalassiosira_oceanica_AB015['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_oceanica_AB015['NumReads_sum_per_million']=Thalassiosira_oceanica_AB015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_oceanica_AB015['NumReads_per_million']=Thalassiosira_oceanica_AB015['NumReads']/Thalassiosira_oceanica_AB015['NumReads_sum_per_million']

#round the dfs
Thalassiosira_oceanica_AB013=Thalassiosira_oceanica_AB013.round(decimals=0)
Thalassiosira_oceanica_AB014=Thalassiosira_oceanica_AB014.round(decimals=0)
Thalassiosira_oceanica_AB015=Thalassiosira_oceanica_AB015.round(decimals=0)

#print the outputs
Thalassiosira_oceanica_AB013.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_oceanica_AB013.txt', sep='\t', index=False)
Thalassiosira_oceanica_AB014.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_oceanica_AB014.txt', sep='\t', index=False)
Thalassiosira_oceanica_AB015.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_oceanica_AB015.txt', sep='\t', index=False)
##########################################################################################
Thalassiosira_punctigera_AB013=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_punctigera_camnt_salmon_quant_AB013_quant.sf', sep='\t')
Thalassiosira_punctigera_AB014=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_punctigera_camnt_salmon_quant_AB014_quant.sf', sep='\t')
Thalassiosira_punctigera_AB015=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_punctigera_camnt_salmon_quant_AB015_quant.sf', sep='\t')
#sum read counts & add to a new column
Thalassiosira_punctigera_AB013['NumReads_sum']=Thalassiosira_punctigera_AB013['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_punctigera_AB013['NumReads_sum_per_million']=Thalassiosira_punctigera_AB013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_punctigera_AB013['NumReads_per_million']=Thalassiosira_punctigera_AB013['NumReads']/Thalassiosira_punctigera_AB013['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_punctigera_AB014['NumReads_sum']=Thalassiosira_punctigera_AB014['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_punctigera_AB014['NumReads_sum_per_million']=Thalassiosira_punctigera_AB014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_punctigera_AB014['NumReads_per_million']=Thalassiosira_punctigera_AB014['NumReads']/Thalassiosira_punctigera_AB014['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_punctigera_AB015['NumReads_sum']=Thalassiosira_punctigera_AB015['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_punctigera_AB015['NumReads_sum_per_million']=Thalassiosira_punctigera_AB015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_punctigera_AB015['NumReads_per_million']=Thalassiosira_punctigera_AB015['NumReads']/Thalassiosira_punctigera_AB015['NumReads_sum_per_million']

#round the dfs
Thalassiosira_punctigera_AB013=Thalassiosira_punctigera_AB013.round(decimals=0)
Thalassiosira_punctigera_AB014=Thalassiosira_punctigera_AB014.round(decimals=0)
Thalassiosira_punctigera_AB015=Thalassiosira_punctigera_AB015.round(decimals=0)

#print the outputs
Thalassiosira_punctigera_AB013.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_punctigera_AB013.txt', sep='\t', index=False)
Thalassiosira_punctigera_AB014.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_punctigera_AB014.txt', sep='\t', index=False)
Thalassiosira_punctigera_AB015.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_punctigera_AB015.txt', sep='\t', index=False)
##########################################################################################
Thalassiosira_rotula_AB013=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_rotula_camnt_salmon_quant_AB013_quant.sf', sep='\t')
Thalassiosira_rotula_AB014=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_rotula_camnt_salmon_quant_AB014_quant.sf', sep='\t')
Thalassiosira_rotula_AB015=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_rotula_camnt_salmon_quant_AB015_quant.sf', sep='\t')
#sum read counts & add to a new column
Thalassiosira_rotula_AB013['NumReads_sum']=Thalassiosira_rotula_AB013['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_rotula_AB013['NumReads_sum_per_million']=Thalassiosira_rotula_AB013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_rotula_AB013['NumReads_per_million']=Thalassiosira_rotula_AB013['NumReads']/Thalassiosira_rotula_AB013['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_rotula_AB014['NumReads_sum']=Thalassiosira_rotula_AB014['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_rotula_AB014['NumReads_sum_per_million']=Thalassiosira_rotula_AB014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_rotula_AB014['NumReads_per_million']=Thalassiosira_rotula_AB014['NumReads']/Thalassiosira_rotula_AB014['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_rotula_AB015['NumReads_sum']=Thalassiosira_rotula_AB015['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_rotula_AB015['NumReads_sum_per_million']=Thalassiosira_rotula_AB015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_rotula_AB015['NumReads_per_million']=Thalassiosira_rotula_AB015['NumReads']/Thalassiosira_rotula_AB015['NumReads_sum_per_million']

#round the dfs
Thalassiosira_rotula_AB013=Thalassiosira_rotula_AB013.round(decimals=0)
Thalassiosira_rotula_AB014=Thalassiosira_rotula_AB014.round(decimals=0)
Thalassiosira_rotula_AB015=Thalassiosira_rotula_AB015.round(decimals=0)

#print the outputs
Thalassiosira_rotula_AB013.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_rotula_AB013.txt', sep='\t', index=False)
Thalassiosira_rotula_AB014.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_rotula_AB014.txt', sep='\t', index=False)
Thalassiosira_rotula_AB015.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_rotula_AB015.txt', sep='\t', index=False)
##########################################################################################
Thalassiosira_sp_AB013=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_sp_camnt_salmon_quant_AB013_quant.sf', sep='\t')
Thalassiosira_sp_AB014=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_sp_camnt_salmon_quant_AB014_quant.sf', sep='\t')
Thalassiosira_sp_AB015=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_sp_camnt_salmon_quant_AB015_quant.sf', sep='\t')
#sum read counts & add to a new column
Thalassiosira_sp_AB013['NumReads_sum']=Thalassiosira_sp_AB013['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_sp_AB013['NumReads_sum_per_million']=Thalassiosira_sp_AB013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_sp_AB013['NumReads_per_million']=Thalassiosira_sp_AB013['NumReads']/Thalassiosira_sp_AB013['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_sp_AB014['NumReads_sum']=Thalassiosira_sp_AB014['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_sp_AB014['NumReads_sum_per_million']=Thalassiosira_sp_AB014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_sp_AB014['NumReads_per_million']=Thalassiosira_sp_AB014['NumReads']/Thalassiosira_sp_AB014['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_sp_AB015['NumReads_sum']=Thalassiosira_sp_AB015['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_sp_AB015['NumReads_sum_per_million']=Thalassiosira_sp_AB015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_sp_AB015['NumReads_per_million']=Thalassiosira_sp_AB015['NumReads']/Thalassiosira_sp_AB015['NumReads_sum_per_million']

#round the dfs
Thalassiosira_sp_AB013=Thalassiosira_sp_AB013.round(decimals=0)
Thalassiosira_sp_AB014=Thalassiosira_sp_AB014.round(decimals=0)
Thalassiosira_sp_AB015=Thalassiosira_sp_AB015.round(decimals=0)

#print the outputs
Thalassiosira_sp_AB013.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_sp_AB013.txt', sep='\t', index=False)
Thalassiosira_sp_AB014.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_sp_AB014.txt', sep='\t', index=False)
Thalassiosira_sp_AB015.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_sp_AB015.txt', sep='\t', index=False)
##########################################################################################
Thalassiosira_weissflogii_AB013=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_weissflogii_camnt_salmon_quant_AB013_quant.sf', sep='\t')
Thalassiosira_weissflogii_AB014=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_weissflogii_camnt_salmon_quant_AB014_quant.sf', sep='\t')
Thalassiosira_weissflogii_AB015=pd.read_table('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_weissflogii_camnt_salmon_quant_AB015_quant.sf', sep='\t')
#sum read counts & add to a new column
Thalassiosira_weissflogii_AB013['NumReads_sum']=Thalassiosira_weissflogii_AB013['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_weissflogii_AB013['NumReads_sum_per_million']=Thalassiosira_weissflogii_AB013['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_weissflogii_AB013['NumReads_per_million']=Thalassiosira_weissflogii_AB013['NumReads']/Thalassiosira_weissflogii_AB013['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_weissflogii_AB014['NumReads_sum']=Thalassiosira_weissflogii_AB014['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_weissflogii_AB014['NumReads_sum_per_million']=Thalassiosira_weissflogii_AB014['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_weissflogii_AB014['NumReads_per_million']=Thalassiosira_weissflogii_AB014['NumReads']/Thalassiosira_weissflogii_AB014['NumReads_sum_per_million']
#sum read counts & add to a new column
Thalassiosira_weissflogii_AB015['NumReads_sum']=Thalassiosira_weissflogii_AB015['NumReads'].sum()
#convert reads to reads per million
Thalassiosira_weissflogii_AB015['NumReads_sum_per_million']=Thalassiosira_weissflogii_AB015['NumReads_sum']/1000000
#divide the reads by the reads per million 
Thalassiosira_weissflogii_AB015['NumReads_per_million']=Thalassiosira_weissflogii_AB015['NumReads']/Thalassiosira_weissflogii_AB015['NumReads_sum_per_million']

#round the dfs
Thalassiosira_weissflogii_AB013=Thalassiosira_weissflogii_AB013.round(decimals=0)
Thalassiosira_weissflogii_AB014=Thalassiosira_weissflogii_AB014.round(decimals=0)
Thalassiosira_weissflogii_AB015=Thalassiosira_weissflogii_AB015.round(decimals=0)

#print the outputs
Thalassiosira_weissflogii_AB013.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_weissflogii_AB013.txt', sep='\t', index=False)
Thalassiosira_weissflogii_AB014.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_weissflogii_AB014.txt', sep='\t', index=False)
Thalassiosira_weissflogii_AB015.to_csv('/Users/joselynn/mmetsp_files/Jan2018_salmon_quants/Thalassiosira_weissflogii_AB015.txt', sep='\t', index=False)

