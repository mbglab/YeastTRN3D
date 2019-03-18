# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 23:28:05 2017

@author: Dongqing
"""

# ----------------------------- Combine FFL and distance of interactions ---------------------------------

# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")

motifs_file = '6-Motif/Result/TRN_dump3_FFL.txt'
gene2num_file = '6-Motif/Result/genename2num.txt'
dist_file = '6-Motif/Data/TRN_dist.txt'

motifs_file_new = '6-Motif/Result/FFL_reg_dist.txt'


int2gene_dict = {}
for line in open(gene2num_file):
    items = line.strip().split('\t')
    int2gene_dict.update({items[1]:items[0]})


interaction_dict = {}
for line in open(dist_file).readlines()[1:]:
    items = line.strip().split('\t')
    gene_pair = [items[0],items[1]]
    gene_pair_dict = {tuple(gene_pair):(items[2],float(items[3]))}
    interaction_dict.update(gene_pair_dict)

bin_pair_set = set(interaction_dict.keys())

nstr = 'FFL_num\tFFL_XYZ\tave\treg\tXY\tXZ\tYZ\n'
for line in open(motifs_file):
    motif = line.strip().split(' ')[0][:-1]
    trn_int_lst = line.strip().split(' ')[1:]
    gene_lst = [int2gene_dict[x] for x in trn_int_lst]
    gene_txt = ''
    for gene in gene_lst:
        gene_txt += gene+' '
    gene_pairs = [(gene_lst[2],gene_lst[1]), (gene_lst[2],gene_lst[0]), (gene_lst[1],gene_lst[0])]
    dist_list = [interaction_dict[gene_pairs[0]][1],interaction_dict[gene_pairs[1]][1],interaction_dict[gene_pairs[2]][1]]
    interaction_dist = str(sum(dist_list)/3)
    dist_list_str = [str(i) for i in dist_list]
    
    reg_info = interaction_dict[gene_pairs[0]][0]+'|'+interaction_dict[gene_pairs[1]][0]+'|'+interaction_dict[gene_pairs[2]][0]
    nline = line[:-1]+'\t'+gene_txt[:-1]+'\t'+interaction_dist+ '\t'+reg_info+'\t'+'\t'.join(dist_list_str)+'\n'
    nstr += nline

nf = open(motifs_file_new,'w')
nf.write(nstr)
nf.close()

