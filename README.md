# shell-scripts
## Metatranscriptome pipeline - relative abundance of metatranscriptome reads
#### 1.) Trim your reads in trimmomatic (use the *_pe_trimmomatic.sh scripts)
```
#!/bin/bash
#SBATCH -t 8:00:00
#SBATCH -n 32
#SBATCH -J ab013_pe_trimmomatic
#SBATCH --mem=64GB
module load trimmomatic/0.32
java -jar $TRIMMOMATIC_BASE/Trimmomatic-0.32/trimmomatic-0.32.jar PE -threads 32  \
/users/jlw578/scratch/reads/AB013_GTGAAA_L008_R1_001.fastq.bz2 /users/jlw578/scratch/reads/AB013_GTGAAA_L008_R2_001.fastq.bz2 \
/users/jlw578/scratch/reads/pe_trim/AB013_forward_paired.fq /users/jlw578/scratch/reads/pe_trim/AB013_forward_singletons.fq /users/jlw578/scratch/reads/pe_trim/AB013_reverse_paired.fq /users/jlw578/scratch/reads/pe_trim/AB013_reverse_singletons.fq \
ILLUMINACLIP:/users/jlw578/scratch/reads/trimmomatic_provided_truseq_adapters.fa:2:30:10 \
HEADCROP:15 \
SLIDINGWINDOW:6:20 \
MINLEN:25
```

#### 2.) The next step was to blast my reads to the MMETSP database using DIAMOND blastx
##### First, make your diamond database (makediamonddb.sh)
```
#!/bin/bash
#SBATCH -t 48:00:00
#SBATCH -n 16
#SBATCH -J makedb_diamond
#SBATCH --mem=64GB
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com
module load diamond/0.8.37
diamond makedb --in /users/jlw578/scratch/mmetsp_oneline_files/mmetsp_ids/prot/output/clustered/concatenated_clustered/concatedated_clustered_mmetsp_prots.txt -d /users/jlw578/data/diamond/mmetsp_98_db -p 16
```

##### Then, blast your trimmed reads to the database (diamond_blastx_ab013_f.sh is one example)
```
#SBATCH -t 48:00:00
#SBATCH -n 16
#SBATCH -J ab013_f_diamond
#SBATCH --mem=64GB
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com
module load diamond/0.8.37
diamond blastx -d /users/jlw578/data/diamond/mmetsp_98_db.dmnd -q /users/jlw578/data/reads/AB013_forward_paired.fq -o /users/jlw578/data/diamond/noevaluecutoff/top0/AB013_forward_paired_out -p 16 -f 6 qseqid sseqid sallseqid evalue bitscore score length pident stitle salltitles qcovhsp qtitle --top 0
```

#### 3.) Use the ab013_forward_script.sh script to analyze the outputs, here's what that script does:
##### First, print column 1 of the AB013_forward_paired_out (this is the read IDs), then sort them and get the lines that only appear once (uniq -u), the output from this is a list of read IDs that only map once (i.e., map uniquely), but you don't yet have the full CAMPEP ID of those sequences....
```
awk '{ print $1 }' AB013_forward_paired_out | sort | uniq -u > AB013_forward_paired_out_uniqu
```
##### Then, use the AB013_forward_paired_out_uniqu file as an input list for fgrep (using the -f flag). Fgrep will use that list to search the file AB013_forward_paired_out for matches and will print out the entire line containing a match (AB013_forward_paired_out_uniqu_full_line).

```
fgrep -f AB013_forward_paired_out_uniqu AB013_forward_paired_out > AB013_forward_paired_out_uniqu_full_line
```
##### The last step in this script just prints the second column (which is the campep IDs). These are the campep IDs that had a DIAMOND blastX read recruit uniquely.
```
awk '{ print $2 }' AB013_forward_paired_out_uniqu_full_line > AB013_forward_paired_out_uniqu_campep_ids
```
#### 4.) Now, I have a list of CAMPEP IDs that had a DIAMOND blastX read recruit uniquely. I'd like to get a handle on the taxonomic distributions of these proteins. The files you need for this are in the Jenkins Lab Drive. The campep_grindstone.txt file contains the campep IDs associated with each campep grindstone ID (like, MMETSP0737 or whatever). The mmetsp_taxonomy.txt file has the taxonomic information associated with each mmetsp grindstone ID.
```
import pandas as pd
campep_grindstone=pd.read_table('/Users/joselynn/Downloads/campep_grindstone.txt', sep='\t')
campep_ids=pd.read_table('/Users/joselynn/Downloads/campep_IDs_of_interest.txt', sep='\t', header=None)
campep_ids.columns=['campep']
campep_ids_grindstone=campep_ids.merge(campep_grindstone, how='inner', on='campep')
mmetsp_taxonomy=pd.read_table('/Users/joselynn/Downloads/mmetsp_taxonomy.txt', sep='\t')
campep_ids_grindstone_taxonomy=campep_ids_grindstone.merge(mmetsp_taxonomy, how='inner', on='grindstone_name')
campep_ids_grindstone_taxonomy.to_csv('/Users/joselynn/Downloads/campep_IDs_of_interest_taxonomy.txt', sep='\t', index=False)
```
##### You can filter so we only look at the diatoms
```
campep_ids_grindstone_taxonomy_Bacillariophyta=campep_ids_grindstone_taxonomy[(campep_ids_grindstone_taxonomy['phylum_name']=='Bacillariophyta')]
```
##### You can then count how many of the transcripts are from the different genera in the table
```
campep_ids_grindstone_taxonomy_Bacillariophyta_genus_count=campep_ids_grindstone_taxonomy_Bacillariophyta.groupby('genus_name').count()
```
##### You can also do more fancy filtering -- here we filter so we only have Skeletonema or Thalassiosira diatoms
```
campep_ids_grindstone_taxonomy_Bacillariophyta_filtered=
campep_ids_grindstone_taxonomy_Bacillariophyta[(campep_ids_grindstone_taxonomy_Bacillariophyta['genus_name']=='Skeletonema')|(campep_ids_grindstone_taxonomy_Bacillariophyta['genus_name']=='Thalassiosira')]
```
##### You can use these outputs to make stacked barcharts in ggplot to visualize the relative abundances.

## Metatranscriptome pipeline - looking at more stringent mapping using BWA
#### 1.) First, make your BWA index
```
#!/bin/bash
#SBATCH -t 8:00:00
#SBATCH -n 32
#SBATCH -J bwa_index_metatranscriptome_diamond_hits
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com
module load bwa/0.7.12
bwa index metatranscriptome_diamond_hits.txt
```
#### 2.) Run the mapping using bwa_mem (AB013, AB014, and AB015 are the shorthand IDs for different libraries I'm comparing)
```
#!/bin/bash
#SBATCH -t 48:00:00
#SBATCH -n 32
#SBATCH -J bwa_mem_ab013_T60
#SBATCH --mail-type=ALL
#SBATCH --mail-user=joselynnw@gmail.com
module load bwa/0.7.12
bwa mem -T 60 -aM -k 10 metatranscriptome_diamond_hits.txt /users/jlw578/scratch/reads/pe_trim/AB013_forward_paired.fq  /users/jlw578/scratch/reads/pe_trim/AB013_reverse_paired.fq > metatranscriptome_diamond_hits_pe_AB013_T60.sam
```

#### 3.) Analyze outputs in samtools -- first convert sam to bam, then sort and index, then run idxstats to get the number of mapped reads per transcript. We might want to change the way these are run to use the SAM flags to filter out non-uniquely mapped reads (rather than using MAPQ60 filtering)
```
interact -t 4:00:00 -m 64g
module load samtools/1.3.1

samtools view -S -b metatranscriptome_diamond_hits_pe_AB013_T60.sam > metatranscriptome_diamond_hits_pe_AB013_T60.bam
samtools sort metatranscriptome_diamond_hits_pe_AB013_T60.bam -o metatranscriptome_diamond_hits_pe_AB013_sorted.bam
samtools index metatranscriptome_diamond_hits_pe_AB013_sorted.bam
samtools idxstats metatranscriptome_diamond_hits_pe_AB013_sorted.bam > metatranscriptome_diamond_hits_pe_AB013_sorted_idxstats_out.txt
```
## ASC notes
#### 1.) Print the transcript IDs and the counts values for each condition into their own separate 1-column text files
#### 2.) Import them into R
```
labels<-read.table("Skeletonema_costatum_all_2tpm_filtered_ids.txt", header=FALSE)
ab013<-read.table("Skeletonema_costatum_all_2tpm_filtered_ab013_cpm.txt", header=FALSE)
ab014<-read.table("Skeletonema_costatum_all_2tpm_filtered_ab014_cpm.txt", header=FALSE)
ab015<-read.table("Skeletonema_costatum_all_2tpm_filtered_ab015_cpm.txt", header=FALSE)
```
#### 3.) Convert them into vectors, use 'trunc' to convert decimals to integers
```
labels<-as.matrix(as.vector(labels))
ab013<-as.matrix(as.vector(trunc(ab013)))
ab014<-as.matrix(as.vector(trunc(ab014)))
ab015<-as.matrix(as.vector(trunc(ab015)))
```

#### 4.) Assign the transcript IDs as labels
```
names(ab013)<-labels
names(ab014)<-labels
names(ab015)<-labels
```
#### 5.) Load the ASC package
```
source("/Users/Joselynn/Dropbox/ASC/asc_0.1.5.R")
```

#### 6.) Run differential expression between the ab013 condition and the ab014 condition
```
dge_ab013_ab014<-DGE(ab013,ab014)
```

#### 7.) Order the outputs based on the delta value
```
kf=order(-abs(dge_ab013_ab014$delta[,1]))[1:4303]
```

#### 8.) Run posterior probability of a 2-fold change
```
postpD=PostProb(dge_ab013_ab014$delta[kf,],ab013[kf], ab014[kf],dge_ab013_ab014$pars,d0=2)
```

#### 9.) Write the output files 
```
write.table(dge_ab013_ab014, "Skeletonema_costatum_all_2tpm_filtered_ab013_ab014_dge", sep="\t")
write.table(kf, "Skeletonema_costatum_all_2tpm_filtered_ab013_ab014_kf", sep="\t")
write.table(postpD, "Skeletonema_costatum_all_2tpm_filtered_ab013_ab014_postpD", sep="\t")
```
## Renaming tree members 
#### This script uses a dictionary to re-name the members of your phylogenetic tree. In theory you could use this type of script to automate renaming files other than trees.
##### "unitprot_dictionary_2.txt" is my dictionary w the things I want to rename and their new names
##### "RAxML_bipartitions.trimmed_alignment_formatted copy 2.tre" is the tree I want to rename 
##### "RAxML_bipartitions.trimmed_alignment_formatted_renamed.tre" is the output file that the script writes
##### Here's the python script:
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 16:57:48 2017
@author: joselynn
"""
u=open("all_bicarbonate_transporters_ids_dictionary.txt", "r+")
uniprot=u.readlines()
u_stripped = [l.rstrip() for l in uniprot]

d={}
for item in u_stripped:
    key, value = item.split('\t')
    d[key]=(value)
    
tree=open("RAxML_bipartitions.bicarbonate_transporter_trimmed.tre", "r+") 
t = tree.read()

#for key in d.iterkeys():
#    t.replace()

for k, v in d.items():
#search in the tree for k     
    t = t.replace(k,v)

f=open("RAxML_bipartitions.bicarbonate_transporter_trimmed_renamed.tre", "w")
f.write(t)
f.close()
```
