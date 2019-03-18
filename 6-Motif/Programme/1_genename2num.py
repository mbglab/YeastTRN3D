# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 13:24:46 2017

@author: Dongqing
"""

# --------------------- Convert the gene name to number ----------------------

# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")

trnfile = '6-Motif/Data/TRN.txt'
outfile1 = '6-Motif/Result/TRN_num.txt'
outfile2 = '6-Motif/Result/genename2num.txt'


genelst = []
for line in open(trnfile):
    items = line.strip().split('\t')
    for gene in items[0:2]:
        if not gene in genelst:
            genelst.append(gene)
            
intdict = {}
i = 0
for gene in genelst:
    i += 1
    item = {gene:str(i)}
    intdict.update(item)

nf1 = open(outfile1, 'w')
for line in open(trnfile):
    genes = line.strip().split('\t')
    if genes[0] != genes[1]:
        nstr = intdict[genes[0]]+'\t'+intdict[genes[1]]+'\t'+'1'+'\n'
        nf1.write(nstr)
nf1.close()

nf2 = open(outfile2, 'w')
for gene in intdict:
    nstr = gene+'\t'+intdict[gene]+'\n'
    nf2.write(nstr)
nf2.close()