# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 14:18:32 2017

@author: Dongqing
"""

# ---------------- Remove remote gene pairs (separated by less than 50kb in the genome) --------------

# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")
import numpy as np

geneFile = '3-Global/Data/AGR_Yeast_Genes.txt'
                
all_file = "3-Global/Result/ALL_dist.txt"
outfile = "3-Global/Result/ALL_remote_dist(50kb).txt"
#outfile = "YEAST/2-TRN+3D/Result/TRN_remote_dist(20kb).txt"


def gene_distance(gene_pair):
    if geneSiteDict[gene_pair[0]][0] == geneSiteDict[gene_pair[1]][0]:
        gene1site = geneSiteDict[gene_pair[0]][1]
        gene2site = geneSiteDict[gene_pair[1]][1]
        gene_d = abs(gene1site - gene2site)
    else:
        gene_d = np.inf
    return gene_d
       


geneSiteDict={}
for line in open(geneFile):
    items = line[:-1].split('\t')
    geneid = items[0]
    if items[2] != '':
        startloc = int(items[3])
        termloc = int(items[4])
        chrom = items[2]
        grd ={geneid:(chrom,(startloc+termloc)/2)}
        geneSiteDict.update(grd)


nf = open(outfile,'w')
n=0
remote_threshold =  50000 #or 20000#50000
for line in open(all_file):
    if "id1" in line:
        nf.write(line)
    if "id1" not in line:
        genes = line.strip().split('\t')
        genepair = genes[:2]
        geneDistance = gene_distance(genepair)
        if geneDistance >= remote_threshold:
            nf.write(line)
            n=n+1
nf.close()

print n

print "ok"