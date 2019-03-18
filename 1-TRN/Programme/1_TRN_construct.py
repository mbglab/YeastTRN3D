# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 15:28:23 2017

@author: Dongqing
"""

#import os
#os.chdir("/Users/dongqing/Desktop/Yeast")

# -------------------------- construct TRN ---------------------------

tot_network = []

tf_tg = '1-TRN/Data/TranscriptionFactor_TargetGene.txt'
tf_tf = '1-TRN/Data/TranscriptionFactor_TranscriptionFactor.txt'
outfile = '1-TRN/Result/TRN_ori.txt'

for line in open(tf_tg):
    items = line.strip().split('\t')
    tf_gname =items[0]
    tg_gname = items[1]
    tf_tg_item = [tf_gname,tg_gname,items[2]]
    if not tf_tg_item in tot_network:
        tot_network.append(tf_tg_item)

tf_tf_network=[]
for line in open(tf_tf):
    items = line.strip().split('\t')
    tf_gname =items[0]
    tf_gname2 = items[1]
    tf_tf_item = [tf_gname,tf_gname2,items[2]]
    if not tf_tf_item in tot_network:
        tot_network.append(tf_tf_item)
    else:
        tf_tf_network.append(tf_tf_item)
        
nf = open(outfile, 'w')
for item in tot_network:
    nstr = '\t'.join(item) + '\n'
    nf.write(nstr)
nf.close()

print "done^_^"

# ------------------------ remove duplicated interactions ---------------------
infile = '1-TRN/Result/TRN_ori.txt'
outfile = '1-TRN/Result/TRN.txt'

interactiondir = {}
for line in open(infile):
    items = line.strip().split('\t')
    tf_tg = (items[0],items[1])
    if not tf_tg in interactiondir:
        interactiondir[tf_tg] = items[2]
    else:
        interactiondir[tf_tg] += '/'+items[2]

nf = open(outfile,'w')

for item in interactiondir:
    reg = interactiondir[item]
    regl=reg.strip().split('/')
    nreg = []
    for signal in regl:
        if not signal in nreg:
            nreg.append(signal)
    nreg.sort()
    if len(nreg)>1:
        if nreg[0]=='+' and nreg[1]=='-':
            nregg=[nreg[0],nreg[1]]
        elif nreg[0]=='+':
            nregg=[nreg[0]]
        elif nreg[0]=='-':
            nregg=[nreg[0]]
        else:
            nregg=nreg
    else:
        nregg=nreg
    strneg ='/'.join(nregg)
    nline = item[0]+'\t'+item[1]+'\t'+strneg+'\n'
    nf.write(nline)
    
nf.close()

print "done^_^"
