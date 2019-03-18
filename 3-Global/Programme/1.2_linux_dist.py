# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 10:31:08 2017

@author: Dongqing
"""

# ------------------------ Calculate the spatial distance of any two genes in the genome --------------------------


# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")
import pandas as pd
import math
import numpy as np

gene_coord_file = "3-Global/Data/gene_coord.txt"
#ALL_gene_file = "D:/3D/YEAST/YEAST/2-TRN+3D/Result/TRN_loc.txt"
#dist_file = "D:/3D/YEAST/YEAST/2-TRN+3D/Result/TRN_dist.txt"
ALL_gene_file = "3-Global/Result/ALL_loc.txt"
dist_file = "3-Global/Result/ALL_dist.txt"

gene_coord = pd.read_table(gene_coord_file,sep="\t")
inter = pd.read_table(ALL_gene_file,sep="\t",usecols=['id1','id2'])

genedict = {}
for i in range(7152):
    gene = {gene_coord.loc[i,'id']:(gene_coord.loc[i,'x'],gene_coord.loc[i,'y'],gene_coord.loc[i,'z'])}
    genedict.update(gene)

def dist(x):
    id1=x[0]
    id2=x[1]
    if genedict.has_key(id1) & genedict.has_key(id2):
        d=math.sqrt(pow((genedict[id1][0]-genedict[id2][0]),2)+pow((genedict[id1][1]-genedict[id2][1]),2)+pow((genedict[id1][2]-genedict[id2][2]),2))
    else:
        d=np.nan
    return d

inter.loc[:,'distance']=inter.apply(dist,axis=1)

def writetostr(x):
    x[2] = "%.3f"%x[2]
    line = '\t'.join(x)
    return line

inter.loc[:,'strline']=inter.apply(writetostr,axis=1)

lines = 'id1\tid2\tdistance\n' + '\n'.join(inter.loc[:,'strline']) + '\n'

dist_result=open(dist_file,'w')
dist_result.write(lines)
dist_result.close()
