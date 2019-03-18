## 3-Global
In this part, the result files are too large to be stored here in github. Please run the code according to the instruction if you want to check the results. 

### a. Calculate the spatial distance of any two genes in the genome
* Input:
  * AGR_Yeast_Genes.txt
  * gene_coord.txt
* Code:
  * 1.1_All_gene_3D.py
  * 1.2_linux_dist.py
* Output: (The two output files are too large to be stored here.)
  * ALL_loc.txt (The genome position of all genes)
  * ALL_dist.txt (The spatial distance of any two genes in the genome)

### b. Remove remote gene pairs (separated by less than 50kb in the genome)
* Input:
  * AGR_Yeast_Genes.txt
  * ALL_dist.txt
* Code:
  * 2_linux_All_remote.py
* Output: (The output file is too large to be stored here.)
  * ALL_remote_dist(50kb).txt

### c. Analyze the global features
* Input:
  * TRN_dist.txt
  * ALL_dist.txt
* Code:
  * 3_TRN_analysis.R
