# ------------------------ Analyze the features ------------------------------


setwd("/Users/dongqing/Desktop/Yeast/")
TRN <- read.table("4-Centrality/Data/TRN_dist.txt",header = TRUE,sep = "\t")
outhub <- read.table("4-Centrality/Result/outhub_all_15.txt",header = TRUE,sep = '\t')
outhub_outhub <- subset(outhub, type == "outhub",select = c("type","distance" ))
outhub_others <- subset(outhub, type == "others",select = c("type","distance" ))
outhub_inter <- subset(outhub, type == "inter" ,select = c("type","distance" ))

mean(outhub_outhub$distance,na.rm=T)
mean(outhub_others$distance,na.rm=T)
mean(outhub_inter$distance,na.rm=T)
mean(TRN$distance,na.rm=T)


wilcox.test(outhub_outhub$distance,TRN$distance)
wilcox.test(outhub_others$distance,TRN$distance,alternative = "less")
wilcox.test(outhub_inter$distance,TRN$distance,alternative = "greater")

wilcox.test(outhub_outhub$distance,outhub$distance,alternative = "greater")
wilcox.test(outhub_others$distance,outhub$distance,alternative = "less")
wilcox.test(outhub_inter$distance,outhub$distance,alternative = "greater")

length(outhub_outhub$distance)
length(outhub_others$distance)
length(outhub_inter$distance)

length(TRN$distance)


plot(density(TRN$distance,na.rm=T),lty=1,xlab="distance",lwd=2)
lines(density(outhub_other$distance,na.rm=T),lty=2,lwd=2)
lines(density(outhub_inter$distance,na.rm=T),lty=3,lwd=2)
lines(density(TRN$distance,na.rm=T),lty=4,lwd=2)
legend("topright",c("+","-","+/-"),lty=c(1,2,3))