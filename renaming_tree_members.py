#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 16:57:48 2017

@author: joselynn
"""

u=open("/Volumes/space/Dropbox/Dropbox/SiPaper/November_2017/atp_grasp/unitprot_dictionary_2.txt", "r+")
uniprot=u.readlines()
u_stripped = [l.rstrip() for l in uniprot]

d={}
for item in u_stripped:
    key, value = item.split('\t')
    d[key]=(value)
    
  
tree=open("/Volumes/space/Dropbox/Dropbox/SiPaper/November_2017/atp_grasp/RAxML_bipartitions.trimmed_alignment_formatted copy 2.tre", "r+") 
t = tree.read()


#for key in d.iterkeys():
#    t.replace()

for k, v in d.items():
#search in the tree for k     
    t = t.replace(k,v)

f=open("/Volumes/space/Dropbox/Dropbox/SiPaper/November_2017/atp_grasp/RAxML_bipartitions.trimmed_alignment_formatted_renamed.tre", "w")
f.write(t)
f.close()