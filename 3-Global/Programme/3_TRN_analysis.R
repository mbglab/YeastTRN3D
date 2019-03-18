# ------------------------- Analyze the global features -----------------------------


setwd("/Users/dongqing/Desktop/Yeast/")
TRN <- read.table("2-TRN+3D/Result/TRN_dist.txt",header = TRUE,sep = "\t")
TRN_reg <- subset(TRN, reg == "+"|reg =="-"|reg =="+/-",select = c("reg","distance" ))
TRN_plus <- subset(TRN_reg, reg == "+",select = c("reg","distance" ))
TRN_sub <- subset(TRN_reg, reg == "-",select = c("reg","distance" ))
TRN_and <- subset(TRN_reg, reg == "+/-",select = c("reg","distance" ))

ALL <- read.table("2-TRN+3D/Result/ALL_dist.txt",header = TRUE,sep = "\t")


mean(TRN_plus$distance)
mean(TRN_sub$distance)
mean(TRN_and$distance)
mean(TRN_reg$distance)
mean(TRN$distance,na.rm=T)
mean(ALL$distance,na.rm=T)

length(TRN_plus$distance)
length(TRN_sub$distance)
length(TRN_and$distance)
length(TRN_reg$distance)
length(TRN$distance)

wilcox.test(TRN$distance,ALL$distance,alternative = "greater")

wilcox.test(TRN_plus$distance,TRN_sub$distance,alternative = "less")
wilcox.test(TRN_plus$distance,TRN$distance,alternative = "less")
wilcox.test(TRN_sub$distance,TRN$distance,alternative = "greater")
