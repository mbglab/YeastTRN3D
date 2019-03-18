# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 00:30:36 2017

@author: Dongqing
"""

# ------------------------- Calculate the spatial distance of the genes with regulatory relationship ------------------------


import pandas as pd
import math
import numpy as np
# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")

gene_coord_file = "2-TRN+3D/Result/gene_coord.txt"
ALL_gene_file = "2-TRN+3D/Result/TRN_loc.txt"
dist_file = "2-TRN+3D/Result/TRN_dist.txt"

#ALL_gene_file = "D:/3D/YEAST/YEAST/3-Global/Result/ALL_loc.txt"
#dist_file = "D:/3D/YEAST/YEAST/3-Global/Result/ALL_dist.txt"

gene_coord = pd.read_table(gene_coord_file,sep="\t")
inter = pd.read_table(ALL_gene_file,sep="\t",usecols=['id1','id2','reg'])

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

#定义一个函数把每行变成一个字符串
def writetostr(x):
    x[3] = "%.3f"%x[3]
    line = '\t'.join(x)
    return line
#在数据框中新添一列存放每一行的字符串
inter.loc[:,'strline']=inter.apply(writetostr,axis=1)

#把新的一列以换行符链接合成一个字符串
lines = 'id1\tid2\treg\tdistance\n' + '\n'.join(inter.loc[:,'strline'])

dist_result=open(dist_file,'w')
dist_result.write(lines)
dist_result.close()



    
 