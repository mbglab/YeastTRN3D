# -*- coding: utf-8 -*-
"""
Created on Mon May 07 15:56:09 2018

@author: Dongqing
"""

# -------------- Calculate the centrality and identify central nodes -----------


# the networkx module we used is Version 1.11
import networkx as nx

# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")

TRN_file = "4-Centrality/Data/TRN_dist.txt"

#outfile = "4-Centrality/Result/inhub_list_all_296.txt"
#outfile1 = "4-Centrality/Result/inhub_all_296.txt"
#
#outfile = "4-Centrality/Result/outhub_list_all_28.txt"
#outfile1 = "4-Centrality/Result/outhub_all_28.txt"
#
#outfile = "4-Centrality/Result/bottleneck_list_all_28.txt"
#outfile1 = "4-Centrality/Result/bottleneck_all_28.txt"

outfile = "4-Centrality/Result/center_list_all_28.txt"
outfile1 = "4-Centrality/Result/center_all_28.txt"


def gene_cent(namelist,geneset):   
    nstr = ''
    for genepair in TRN_list:
        if genepair[0] in geneset and genepair[1] in geneset:
            name = namelist[0]
        elif genepair[0] not in geneset and genepair[1] not in geneset:
            name = namelist[1]
        elif genepair[0] in geneset and genepair[1] not in geneset:
            name = namelist[2]
        elif genepair[0] not in geneset and genepair[1] in geneset:
            name = namelist[2]
        else:
            continue
        id1 = genepair[0]
        id2 = genepair[1]
        dist = genepair[2]
        nline = name+'\t'+id1+'\t'+id2+'\t'+dist+'\n'
        nstr += nline
    return nstr

TRN_list = []
for line in open(TRN_file):
    items = line.strip().split('\t')
    if items[0] !='id1':
        TRN_item = []
        TRN_item.append(items[0])
        TRN_item.append(items[1])
        TRN_item.append(items[3])
        TRN_list.append(TRN_item)
print "load TRN__dist success!"

TRN = nx.DiGraph()
edge_list = []
for line in open(TRN_file):
    genepair = line.strip().split('\t')
    if genepair[0]!='id1':
        edge_list.append((genepair[0],genepair[1],1))
TRN.add_weighted_edges_from(edge_list)

print "load TRN success" 
print TRN.number_of_nodes()
print TRN.number_of_edges()

in_cen = sorted(nx.in_degree_centrality(TRN).items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
out_cen = sorted(nx.out_degree_centrality(TRN).items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
bet_cen = sorted(nx.betweenness_centrality(TRN).items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
clo_cen = sorted(nx.closeness_centrality(TRN).items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

centrality = in_cen
centrality = out_cen
centrality = bet_cen
centrality = clo_cen

#cutoff = 296
cutoff = 28

centlst = open(outfile,'w')
for line in centrality[:cutoff]:
    nstr = line[0]+'\t'+str(line[1])+'\n'
    centlst.write(nstr)
centlst.close()

cent = []
for item in centrality[:cutoff] :
    cent.append(item[0])


#namelist = ['inhub','others','inter']
#namelist = ['outhub','others','inter']
#namelist = ['bottleneck','others','inter']
namelist = ['center','others','inter']


nline=''
result = open(outfile1,'w')
tmp = gene_cent(namelist,cent)
nline += tmp
nstr = "type\tid1\tid2\tdistance\n"
nstr = nstr+nline 
result.write(nstr)
result.close()
