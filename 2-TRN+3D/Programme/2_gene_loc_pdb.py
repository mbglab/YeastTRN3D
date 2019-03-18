# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 13:29:44 2017

@author: Dongqing
"""

# --------------- Determine the 3D coordinate of all genes in the genome and determine the index of genes in the pdb file -----------------


import pandas as pd
import numpy as np
# import os

# os.chdir("/Users/dongqing/Desktop/Yeast")


#infile
gene_file = '2-TRN+3D/Data/AGR_Yeast_Genes.txt'
pdb_file = '2-TRN+3D/Data/pdb.txt'
genome_file = '2-TRN+3D/Data/genomic position_3d coordinate.txt'


#outfile
gene_pdbindex="2-TRN+3D/Result/gene_pdbindex.txt"
gene_coord="2-TRN+3D/Result/gene_coord.txt"


genome_3D=pd.read_table(genome_file,sep="\t")


x=[]
y=[]
z=[]
for line in open(pdb_file):
    items = line.strip().split('\t')
    x.append("%.3f"%float(items[5]))
    y.append("%.3f"%float(items[6]))
    z.append("%.3f"%float(items[7]))
    
pdbxyz = np.array([x,y,z]).transpose()
pdb_df = pd.DataFrame(pdbxyz)


genedict={}
for line in open(gene_file):
    items = line[:-1].split('\t')
    geneid = items[0]
    if items[2] != '':
        startloc = int(items[3])
        termloc = int(items[4])
        chrom = items[2]
        grd ={geneid:(chrom,(startloc+termloc)/2)}
        genedict.update(grd)

        
geneloc={}
genecoord={}
for gene in genedict:
    pos=genedict[gene]
    if pos[0]!='chrmt':
        index=genome_3D[genome_3D['chrom'].isin([int(pos[0])])]
        index.loc[:,'absdif']=index['locus'].values-pos[1]
        index.loc[:,'absdif']=index['absdif'].abs()
        mindex=index['absdif'].idxmin()
        coordx=genome_3D.ix[mindex,2]
        coordy=genome_3D.ix[mindex,3]
        coordz=genome_3D.ix[mindex,4]
        gloc={gene:(coordx,coordy,coordz)}
        geneloc.update(gloc)
        pdbindexx=pdb_df[pdb_df.loc[:,0].isin(["%.3f"%coordx])]
        pdbindexy=pdb_df[pdb_df.loc[:,1].isin(["%.3f"%coordy])]
        pdbindexz=pdb_df[pdb_df.loc[:,2].isin(["%.3f"%coordz])]
        pdbindex=set(pdbindexx.index)&set(pdbindexy.index)&set(pdbindexz.index)
        if len(list(pdbindex))!=0:
            pdbindex_lst=list(pdbindex)
        elif set(pdbindexx.index)&set(pdbindexy.index):
            pdbindex_lst=list(set(pdbindexx.index)&set(pdbindexy.index))
        elif set(pdbindexy.index)&set(pdbindexz.index):
            pdbindex_lst=list(set(pdbindexy.index)&set(pdbindexz.index))
        elif set(pdbindexx.index)&set(pdbindexz.index):
            pdbindex_lst=list(set(pdbindexx.index)&set(pdbindexz.index))
        gcoord={gene:pdbindex_lst[0]}
        genecoord.update(gcoord)

nline='id\tpdbindex\n'        
for gene in genecoord:
    nline += gene+ '\t' + str(genecoord[gene]) + '\n'

genepdb_result = open(gene_pdbindex,'w')
genepdb_result.write(nline)
genepdb_result.close()

nline3='id\tx\ty\tz\n'        
for gene in geneloc:
    nline3 += gene+ '\t' + str(geneloc[gene][0]) + '\t' + str(geneloc[gene][1]) + '\t' + str(geneloc[gene][2])+ '\n'

genecoord_result = open(gene_coord,'w')
genecoord_result.write(nline3)
genecoord_result.close()
