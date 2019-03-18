# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:33:03 2017

@author: Dongqing
"""

# ----------------------- Combine TRN with hierarchical level --------------------

# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")

trnfile = 'D:/3D/YEAST/YEAST/5-Hierarchy/Data/TRN_dist.txt'
hierfile = 'D:/3D/YEAST/YEAST/5-Hierarchy/Result/Hierarchical_level.txt'
outfile = 'D:/3D/YEAST/YEAST/5-Hierarchy/Result/hir_3d.txt'

gene_list=[]        
for line in open(trnfile).readlines()[1:]:
    genepair = line.strip().split('\t')[0:2]
    for geneid in genepair:
        if not geneid in gene_list:
            gene_list.append(geneid)

hir_dict = {}
for line in open(hierfile):
    items = line.strip().split(':')
    hier = items[0]
    for genes in items[1].split(','):
        geneid = genes.strip()
        hir_item = {geneid:hier}
        hir_dict.update(hir_item)

for geneid in gene_list:
    if not geneid in hir_dict:
        hir_item = {geneid:'Target'}
        hir_dict.update(hir_item)

nstr = "id1\tid2\thier1\thier2\tdistance\n"
for line in open(trnfile).readlines()[1:]:
    genepair = line.strip().split('\t')
    id1 = genepair[0]
    id2 = genepair[1]
    hir1 = hir_dict[id1]
    hir2 = hir_dict[id2]
    nline = id1+'\t'+id2+'\t'+hir1+'\t'+hir2+'\t'+genepair[3]+'\n'
    nstr += nline

nf = open(outfile,'w')
nf.write(nstr)
nf.close()