# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 18:23:36 2018

@author: Dongqing
"""

# --------- Calculate the mean and SD of distance in each SIM ------------

# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")

sim_file = '6-Motif/Result/SIM.txt'
TRN_file = '6-Motif/Data/TRN_dist.txt'
#TRN_file = '6-Motif/Data/TRN_remote_dist(50kb).txt'

out_file = '6-Motif/Result/SIM_dist_sd.txt'
#out_file = '6-Motif/Result/SIM_remote_dist_var.txt'

import numpy as np
import math

def sam_sd(nlist):
    narray = np.array(nlist)
    nmean = narray.mean()
    nsum = 0.0
    for n in narray:
        nsum += (n-nmean)**2
    nvar = nsum/(len(nlist)-1)
    nsd = math.sqrt(nvar)
    return nsd

dist_dict = {}
reg_dict = {}
self_reg = []
for line in open(TRN_file).readlines()[1:]:
    items = line.strip().split('\t')
    if items[3] != 'nan':
        genepair = (items[0],items[1])
        dist_dict[genepair] = items[3]
        reg_dict[genepair] = items[2]
    if items[0] == items[1]:
        self_reg.append(items[0])


result = open(out_file,'w')
nline = 'SIM\tis_self\treg\tdist_ave\tdist_sd\n'
result.write(nline)
for line in open(sim_file):
    items = line.strip().split('\t')
    parent = items[0]
    children = items[1].strip().split(' ')
    reg = ''
    dist_list = []
    for child in children:
        child_dist = dist_dict.get((parent,child),'')
        if child_dist !='':
            dist_list.append(float(child_dist))
            reg += reg_dict[(parent,child)] + '|'
    if len(dist_list) >1:
        dist_array = np.array(dist_list)
        if parent in self_reg:
            is_self = 'T'
        else:
            is_self = 'F'
        nline = parent+'\t'+is_self+'\t'+reg+'\t'+str(np.mean(dist_array))+'\t'+str(sam_sd(dist_list))+'\n'
        result.write(nline)

result.close()