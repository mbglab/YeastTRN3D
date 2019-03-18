# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 09:42:51 2017

@author: Dongqing
"""

# ------------------------ Determine the genome position of genes -------------------------- 


# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")
gene_file = '3-Global/Data/AGR_Yeast_Genes.txt'
ALL_loc= '3-Global/Result/ALL_loc.txt'

genedict={}
for line in open(gene_file):
    items = line[:-1].split('\t')
    geneid = items[0]
    if items[2] != '':
        startloc = int(items[3])
        termloc = int(items[4])
        chrom = items[2]
        grd ={geneid:(chrom,(startloc+termloc)/2)}
        genedict.update(grd)

k=0
nline1 = "id1\tid2\tchr1\tloc1\tchr2\tloc2\n"
for i in genedict:
    for j in genedict:   
        id1 = i
        id2 = j
        pos1 = genedict[id1]
        pos2 = genedict[id2]
        chr1=pos1[0]
        loc1=pos1[1]
        chr2=pos2[0]
        loc2=pos2[1]
        nstr = id1+'\t'+id2+'\t'+chr1+'\t'+str(loc1)+'\t'+chr2 +'\t'+str(loc2)+'\n'
        nline1 += nstr
        k= k+1
print str(k)

ALL_result = open(ALL_loc,'w')
ALL_result.write(nline1)
ALL_result.close()
print "done"