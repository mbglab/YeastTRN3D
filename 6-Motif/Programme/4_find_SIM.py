# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 18:01:06 2018

@author: Dongqing
"""

# ----------------- Idnetify SIMs in the TRN -----------------


import networkx as nx
# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")

TRN_file = '6-Motif/Data/TRN_dist.txt'
sim_file = '6-Motif/Result/SIM.txt'

TRN = nx.DiGraph()
node_list = []
for line in open(TRN_file).readlines()[1:]:
    genepair = line.strip().split('\t')
    if genepair[0] != genepair[1]:
        node_list.append((genepair[0],genepair[1],1))
TRN.add_weighted_edges_from(node_list)
print "load TRN successfuly"

sim_dict = {}
for node in TRN.nodes():
    induced_c = []
    childs_list = TRN[node].keys()
    for child in childs_list:
        if TRN.in_degree(child) == 1:
            induced_c.append(child)
    if len(induced_c) >= 2:
        sim_dict[node] = induced_c
 
result = open(sim_file,"w")
for item in sim_dict.keys():
    nstr = item+'\t'+' '.join(sim_dict[item])+'\n'
    result.write(nstr)
result.close()    