# ------------------------------ Analyze the features of FFLs -------------------------------


setwd("/Users/dongqing/Desktop/Yeast/")
TRN_re <- read.table("2-TRN+3D/Result/TRN_dist.txt",header = TRUE,sep = "\t")
TRN_reg_re <- subset(TRN_re, reg == "+"|reg =="-"|reg =="+/-",select = c("reg","distance" ))
TRN_plus_re <- subset(TRN_reg_re, reg == "+",select = c("reg","distance" ))
TRN_sub_re <- subset(TRN_reg_re, reg == "-",select = c("reg","distance" ))

mean(TRN_re$distance,na.rm=T)
mean(TRN_plus_re$distance)
mean(TRN_sub_re$distance)

FFL <- read.table("6-Motif/Result/FFL_reg_dist.txt",header = TRUE,sep = "\t")
FFL_reg <- subset(FFL, reg == "+|+|+"|reg =="+|+|-",select = c("reg","ave" ))
FFL_3plus <- subset(FFL,reg == "+|+|+",select = c("ave","XY","XZ","YZ"))
FFL_2plus <- subset(FFL,reg == "+|+|-",select = c("ave","XY","XZ","YZ"))

mean(FFL$ave,na.rm=T)
wilcox.test(FFL$ave,TRN$distance,alternative = "greater")
wilcox.test(FFL_3plus$ave,TRN$distance,alternative = "less")
wilcox.test(FFL_2plus$ave,TRN$distance,alternative = "greater")


mean(FFL_3plus$XY)
mean(FFL_3plus$XZ)
mean(FFL_3plus$YZ)
wilcox.test(FFL_3plus$XY,FFL_3plus$XZ,alternative = "less")
wilcox.test(FFL_3plus$XZ,FFL_3plus$YZ,alternative = "greater")
wilcox.test(FFL_3plus$XY,FFL_3plus$YZ,alternative = "less")
wilcox.test(FFL_3plus$XY,TRN_plus_re$distance,alternative = "less")
wilcox.test(FFL_3plus$XZ,TRN_plus_re$distance)
wilcox.test(FFL_3plus$YZ,TRN_plus_re$distance,alternative = "less")


FFL_2plus <- subset(FFL,reg == "+|+|-",select = c("ave","XY","XZ","YZ"))
mean(FFL_2plus$XY)
mean(FFL_2plus$XZ)
mean(FFL_2plus$YZ)
wilcox.test(FFL_2plus$XY,FFL_2plus$XZ,alternative = "greater")
wilcox.test(FFL_2plus$XZ,FFL_2plus$YZ)
wilcox.test(FFL_2plus$XY,FFL_2plus$YZ)

wilcox.test(FFL_2plus$XY,TRN_plus$distance,alternative = "greater")
wilcox.test(FFL_2plus$XZ,TRN_plus$distance)
wilcox.test(FFL_2plus$YZ,TRN_sub$distance)


