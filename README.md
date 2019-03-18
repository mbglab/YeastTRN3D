# YeastTRN3D
There are six folders in the current path, and each of them has three subfolders named Data, Programme and Result, which store the input, code and output at every step, respectively.


## 1-TRN
Construct TRN and integrate edges with the same nodes but the different direction.
* Input:
  * TranscriptionFactor_TargetGene.txt (TF-TG interaction, derived from SGD database)
  * TranscriptionFactor_TranscriptionFactor.txt (TF-TF interaction, derived from SGD database)
* Code:
  * 1_TRN_construct.py
* Output:
  * TRN_ori.txt (TRN with duplicated edges)
  * TRN.txt (TRN without duplicated interactions)  
  In the file 'TRN.txt', there are three columns -- TF, TG and regulatory direction.


## 2-TRN+3D
Combine TRN and 3D model of the yeast
### a. Determine the genome position of genes participating in TRN
* Input:
  * TRN.txt
  * AGR_Yeast_Genes.txt (genome annotation)
* Code:
  * 1_TRN_loc.py
* Output:
  * TRN_loc.txt (TRN with the genome locations)

### b. Determine the 3D coordinate of all genes in the genome and determine the index of genes in the pdb file
* Input:
  * AGR_Yeast_Genes.txt (derived from SGD database)
  * pdb.txt (3D structure of the yeast which can be shown with RasMol, derived from the study of Duan (2010, Nature))
  * genomic position_3d coordinate.txt (genome position and respective 3D coordinate, derived from the study of Duan (2010, Nature))
* Code:
  * 2_gene_loc.py
* Output:
  * gene_pdbindex.txt (The index of genes in the pdb file)
  * gene_coord.txt (The 3D coordinate of all genes in the genome)

### c. Calculate the spatial distance of the genes with regulatory relationship
* Input:
  * gene_coord.txt
  * TRN_loc.txt
* Code:
  * 3_dist.py
* Output:
  * TRN_dist.txt (The spatial distance of each interaction in the TRN)

### d. Remove remote regulation (separated by less than 50kb in the genome)
* Input:
  * AGR_Yeast_Genes.txt
  * TRN_dist.txt
* Code:
  * 4_TRN_remote.py
* Output:
  * TRN_remote_dist(50kb).txt


## 3-Global
### a. Calculate the spatial distance of any two genes in the genome
* Input:
  * AGR_Yeast_Genes.txt
  * gene_coord.txt
* Code:
  * 1.1_All_gene_3D.py
  * 1.2_linux_dist.py
* Output:
  * ALL_loc.txt (The genome position of all genes)
  * ALL_dist.txt (The spatial distance of any two genes in the genome)

### b. Remove remote gene pairs (separated by less than 50kb in the genome)
* Input:
  * AGR_Yeast_Genes.txt
  * ALL_dist.txt
* Code:
  * 2_linux_All_remote.py
* Output:
  * ALL_remote_dist(50kb).txt

### c. Analyze the global features
* Input:
  * TRN_dist.txt
  * ALL_dist.txt
* Code:
  * 3_TRN_analysis.R


## 4-Centrality
### a. Calculate the centrality and identify central nodes
* Input:
  * TRN_dist.txt
* Code:
  * 1_centrality_all.py
* Output:
  * inhub_all_296.txt (TRN with the information of in-degree centrality)  
  inhub_list_all_296.txt (Inhub nodes and their in-degree centrality)
  * outhub_all_28.txt (TRN with the information of out-degree centrality)  
  outhub_list_all_28.txt (Outhub nodes and their out-degree centrality)
  * bottleneck_all_28.txt (TRN with the information of betweenness centrality)  
  bottleneck_list_all_28.txt (Bottleneck nodes and their betweenness centrality)
  * center_all_28.txt (TRN with the information of closeness centrality)  
  center_list_all_28.txt (Center nodes and their closeness centrality)

### b. Analyze the features
* Input:
  * TRN_dist.txt
  * inhub_all_296.txt
  * outhub_all_28.txt
  * bottleneck_all_28.txt
  * center_all_28.txt
* Code:
  * 2.1_inhub_analysis.R
  * 2.2_outhub_analysis.R
  * 2.3_bottleneck_analysis.R
  * 2.4_center_analysis.R


## 5-Hierarchy
### a. Find TGs and TFs, and generate TF sub-network
* Input:
  * TRN_dist.txt
* Code:
  * 1_Find_TG.py
* Output:
  * Target_genes.txt (Target genes)
  * TRUE_TF.txt (Transcription factors)
  * TRN_TFonly_dist.txt (TF sub-network)

### b. Find isolated TFs neither regulating other TFs nor regulated by other TFs
* Input:
  * TRUE_TF.txt
  * TRN_TFonly_dist.txt
* Code:
  * 2_Find_isolatedTF.py
* Output:
  * isolated_TF.txt (isolated TFs)

### c. Identify all the strongly connected components (SCCs) in the sub-network
* Input:
  * TRN_TFonly_dist.txt
  * isolated_TF.txt
* Code:
  * 3_Find_SCC.py
* Output:
  * SCC.txt (Strongly connected components)

### d. Collapse every SCC into a super node
* Input:
  * TRN_TFonly_dist.txt
  * SCC.txt
* Code:
  * 4_Collapse_SCC.py
* Output:
  * TRN_TF_SCC.txt (TRN with every SCC collapsed into a super node)

### e. Determine the hierarchical level of the genes
* Input:
  * SCC.txt
  * TRN_TF_SCC.txt
  * TRUE_TF.txt
* Code:
  * 5_Hierarchical_level.py
* Output:
  * Hierarchical_level.txt (TFs and their corresponding hierarchical level)

### f. Combine TRN with hierarchical level
* Input:
  * TRN_dist.txt
  * Hierarchical_level.txt
* Code:
  * 6_Hierarchy_3D.py
* Output:
  * hir_3d.txt (TRN with the information of hierarchy)

### g. Analyze the hierarchical features
* Input:
  * hir_3d.txt
* Code:
  * 7_Hierarchy_analysis.R


## 6-Motif
### a. Convert the gene name to number
* Input:
  * TRN.txt
* Code:
  * 1_genename2num.py
* Output:
  * TRN_num.txt (TRN with gene name converted to number)
  * genename2num.txt (Gene name and corresponding number)

### b. Combine FFL and distance of interactions
* Input:
  * TRN_dump3_FFL.txt (FFLs detected by Mfinder)
  * genename2num.txt
  * TRN_dist.txt
* Code:
  * 2_FFL_interaction_dist.py
* Output:
  * FFL_reg_dist.txt (FFLs with distance)

### c. Analyze the features of FFLs
* Input:
  * TRN_dist.txt
  * FFL_reg_dist.txt
* Code:
  * 3_FFL_analysis.R

### d. Idnetify SIMs in the TRN
* Input:
  * TRN_dist.txt
* Code:
  * 4_find_SIM.py
* Output:
  * SIM.txt

### e. Calculate the mean and SD of distance in each SIM 
* Input:
  * SIM.txt
  * TRN_dist.txt
* Code:
  * 5_SIM_stat.py
* Output:
  * SIM_dist_sd.txt (SIM with the information of distance)

### f. Analyze the features of SIM
* Input:
  * TRN_dist.txt
  * SIM_dist_sd.txt
* Code:
  * 6_SIM_analysis.R

