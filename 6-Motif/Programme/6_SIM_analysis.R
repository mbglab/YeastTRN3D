# ---------------------- Analyze the features of SIM ----------------------


setwd("/Users/dongqing/Desktop/Yeast/")
TRN <- read.table("2-TRN+3D/Result/TRN_dist.txt",header = TRUE,sep = "\t")
SIM <- read.table("6-Motif/Result/SIM_dist_sd.txt",header = TRUE,sep = "\t")

mean(TRN$distance,na.rm=T)
mean(SIM$dist_ave,na.rm=T)
vv=sd(TRN$distance,na.rm=T)

wilcox.test(SIM$dist_ave,TRN$distance)
wilcox.test(SIM$dist_sd, mu=vv, alternative="less")

