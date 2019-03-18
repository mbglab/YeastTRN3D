# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:07:53 2017

@author: Dongqing
"""

# ------------------ Collapse every SCC into a super node -----------------

# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")

sccfile = 'D:/3D/YEAST/YEAST/5-Hierarchy/Result/SCC.txt'
trnfile = 'D:/3D/YEAST/YEAST/5-Hierarchy/Result/TRN_TFonly_dist.txt'
outfile = 'D:/3D/YEAST/YEAST/5-Hierarchy/Result/TRN_TF_SCC.txt'

sccdict = {}
for line in open(sccfile):
    items = line.split('\t')
    for gene in items[1].split(','): 
        sccitem = {gene.strip():items[0]}
        sccdict.update(sccitem)
#print sccdict,len(sccdict)

#将以基因名表示的TRN转化为SCC表示的TRN
trnscclst = []
for line in open(trnfile).readlines()[1:]:
    items = line.strip().split('\t')
    nitem = [sccdict.get(items[0], items[0]), sccdict.get(items[1], items[1])]
    if not nitem in trnscclst:
        trnscclst.append(nitem)

nf = open(outfile, 'w')
for item in trnscclst:
    nstr = item[0]+'\t'+item[1]+'\n'
    nf.write(nstr)
nf.close()