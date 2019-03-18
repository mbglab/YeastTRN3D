# ------------------------ Analyze the features ------------------------------


setwd("/Users/dongqing/Desktop/Yeast/")
TRN <- read.table("4-Centrality/Data/TRN_dist.txt",header = TRUE,sep = "\t")
center <- read.table("4-Centrality/Result/center_all_15.txt",header = TRUE,sep = '\t')
center_center <- subset(center, type == "center",select = c("type","distance" ))
center_other <- subset(center, type == "others",select = c("type","distance" ))
center_inter <- subset(center, type == "inter",select = c("type","distance" ))

mean(center_center$distance,na.rm=T)
mean(center_other$distance,na.rm=T)
mean(center_inter$distance,na.rm=T)
mean(TRN$distance,na.rm=T)

wilcox.test(center_center$distance,center$distance)
wilcox.test(center_other$distance,center$distance)
wilcox.test(center_inter$distance,center$distance,alternative = "greater")

length(center_center$distance)
length(center_other$distance)
length(center_inter$distance)
length(TRN$distance)


plot(density(TRN$distance,na.rm=T),lty=1,xlab="distance",lwd=2)
lines(density(center_other$distance,na.rm=T),lty=2,lwd=2)
lines(density(center_inter$distance,na.rm=T),lty=3,lwd=2)
lines(density(TRN$distance,na.rm=T),lty=4,lwd=2)
legend("topright",c("+","-","+/-"),lty=c(1,2,3))