# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 17:12:18 2017

@author: Dongqing
"""

# ----------------------- Determine the genome position of genes participating in TRN ----------------------


# import os
# os.chdir("/Users/dongqing/Desktop/Yeast")

gene_file = '2-TRN+3D/Data/AGR_Yeast_Genes.txt'
TRN_file = '2-TRN+3D/Data/TRN.txt'
TRN_loc= '2-TRN+3D/Result/TRN_loc.txt'

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

n=''
# TRN-3D
nline1 = "id1\tid2\treg\tchr1\tloc1\tchr2\tloc2\n"
for line in open(TRN_file):
    items = line.strip().split('\t')
    id1 = items[0]
    id2 = items[1]
    if genedict.has_key(id1) and genedict.has_key(id2):
        pos1 = genedict[id1]
        pos2 = genedict[id2]
        chr1=pos1[0]
        loc1=pos1[1]
        chr2=pos2[0]
        loc2=pos2[1]
        nstr = '\t'.join(items)+'\t'+chr1+'\t'+str(loc1)+'\t'+chr2 +'\t'+str(loc2)+'\n'
        nline1 += nstr
    elif genedict.has_key(id1)==False:
        n+=id1+'\n'
    elif genedict.has_key(id2)==False:
        n+=id2+'\n'
        
TRN_result = open(TRN_loc,'w')
TRN_result.write(nline1)
TRN_result.close()

#nogene='2-TRN+3D/Result/nogene_list.txt'
#nogene_list=open(nogene,'w')
#nogene_list.write(n)
#nogene_list.close()

print "done^_^"