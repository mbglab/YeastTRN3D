# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:32:48 2017

@author: Dongqing
"""

# -------------------------- Determine the hierarchical level of the genes ---------------------

# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")

sccfile = 'D:/3D/YEAST/YEAST/5-Hierarchy/Result/SCC.txt'
trnfile = 'D:/3D/YEAST/YEAST/5-Hierarchy/Result/TRN_TF_SCC.txt'
tf_set = 'D:/3D/YEAST/YEAST/5-Hierarchy/Data/TRUE_TF.txt'

hirfile = 'D:/3D/YEAST/YEAST/5-Hierarchy/Result/Hierarchical_level.txt'

tflst = []
for line in open(tf_set):
    tflst.append(line.strip())

lst1 = []
lst2 = []
selfloop = []
for line in open(trnfile).readlines():
    items = line.strip().split('\t')
    if items[0] == items[1]:
        selfloop.append(items[0])
    else:
        lst1.append(items[0])
        lst2.append(items[1])

set1 = set(lst1)
set2 = set(lst2)

sccdict = {}
for line in open(sccfile):
    items = line.split('\t')
    sccdict.update({items[0]:items[1]})

toplst = []
middlelst = []
bottomlst = []
for item in set1:
    if item in set2:
        genes =  sccdict.get(item, item)
        for gene in genes.split(','):
            middlelst.append(gene.strip())
    else:
        genes =  sccdict.get(item, item)
        for gene in genes.split(','):
            toplst.append(gene.strip())

for tf in tflst:
    if not tf in toplst:
        if not tf in middlelst:
            bottomlst.append(tf)

toplst.sort()
middlelst.sort()
bottomlst.sort()

nf = open(hirfile, 'w')
str1 = 'Top: '
for tf in toplst:
    str1 += tf+', '
nf.write(str1[:-2]+'\n')
str2 = 'Middle: '
for tf in middlelst:
    str2 += tf+', '
nf.write(str2[:-2]+'\n')
str3 = 'Bottom: '
for tf in bottomlst:
    str3 += tf+', '
nf.write(str3[:-2]+'\n')
nf.close()