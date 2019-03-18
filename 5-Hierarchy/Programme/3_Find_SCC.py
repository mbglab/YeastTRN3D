# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:17:22 2017

@author: Dongqing
"""

# --------------- Identify all the strongly connected components (SCCs) in the sub-network -----------

# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")

trnfile = '5-Hierarchy/Result/TRN_TFonly_dist.txt'
orphan_file = '5-Hierarchy/Result/isolated_TF.txt'
sccfile = '5-Hierarchy/Result/SCC.txt'

import networkx as nx

G = nx.DiGraph()

for line in open(trnfile).readlines()[1:]:
    items = line.strip().split('\t')
    G.add_edge(items[0], items[1])
#print G.edges()

orphan = open(orphan_file)
orphan_list = []
for line in orphan:
    orphan_list.append(line.strip())
#print orphan_list
    
k = nx.strongly_connected_component_subgraphs(G,copy=True)

scc = open(sccfile,'w')
n = 1
for i in k:
    if i.edges() != []: #去除孤立的TF
        nstr = 'S'+str(n)+'\t'+str(i.nodes())+'\t'+str(i.edges())+'\n'
        nstr = nstr.replace("[" ,"").replace("]",'').replace('\'','')
        scc.write(nstr)
        n+=1
scc.close()