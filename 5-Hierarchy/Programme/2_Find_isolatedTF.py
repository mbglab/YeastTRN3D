# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 14:32:02 2017

@author: Dongqing
"""

# --------- Find isolated TFs neither regulating other TFs nor regulated by other TFs ------------

# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")

tffile = '5-Hierarchy/Data/TRUE_TF.txt'
tf_trnfile = '5-Hierarchy/Result/TRN_TFonly_dist.txt'
outfile = '5-Hierarchy/Result/isolated_TF.txt'

tflst = []
for line in open(tffile):
    tflst.append(line.strip())
tfset = set(tflst)

tflst2 = []
for line in open(tf_trnfile).readlines()[1:]:
    genes=line.strip().split('\t')
    tflst2.append(genes[0])
    tflst2.append(genes[1])
tfset2 = set(tflst2)

nf = open(outfile,'w')
for tf in tfset:
    if not tf in tfset2:
        nf.write(tf+'\n')
nf.close()
