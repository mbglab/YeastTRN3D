# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:57:39 2017

@author: Dongqing
"""

# --------------------- Find TGs and TFs, and generate TF sub-network ---------------------

# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")

regulonfile = '5-Hierarchy/Data/TRN_dist.txt'

tgfile = '5-Hierarchy/Result/Target_genes.txt'
true_tf_file = '5-Hierarchy/Result/TRUE_TF.txt'
tf_trn_file = '5-Hierarchy/Result/TRN_TFonly_dist.txt'

tglst = []
tflst1 = []
for line in open(regulonfile).readlines()[1:]:
    items = line.strip().split('\t')
    tf = items[0]
    tg = items[1]
    if not tf in tflst1:
        tflst1.append(tf)
    if not tg in tglst:
        tglst.append(tg)
tfset1 = set(tflst1)

true_tglst = []
for gene in tglst:
    if not gene in tfset1:
        true_tglst.append(gene)

nf1 = open(tgfile, 'w')
for gene in true_tglst:
    nf1.write(gene+'\n')
nf1.close()

tgset = set(true_tglst)
nf2 = open(tf_trn_file, 'w')
nf2.write('id1\tid2\treg\tdistance\n')
for line in open(regulonfile).readlines()[1:]:
    items = line.strip().split('\t')
    items2=items[0:2]
    if not set(items2) & tgset:
        nf2.write(line)
nf2.close()

nf3 = open(true_tf_file, 'w')
for i in tflst1:
    nf3.write(i+'\n')
nf3.close()