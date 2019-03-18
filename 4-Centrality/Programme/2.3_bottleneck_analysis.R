# ------------------------ Analyze the features ------------------------------


setwd("/Users/dongqing/Desktop/Yeast/")
TRN <- read.table("4-Centrality/Data/TRN_dist.txt",header = TRUE,sep = "\t")
bottleneck <- read.table("4-Centrality/Result/bottleneck_all_15.txt",header = TRUE,sep = '\t')
bottleneck_bottleneck <- subset(bottleneck, type == "bottleneck",select = c("type","distance" ))
bottleneck_other <- subset(bottleneck, type == "others",select = c("type","distance" ))
bottleneck_inter <- subset(bottleneck, type == "inter",select = c("type","distance" ))

mean(bottleneck_bottleneck$distance,na.rm=T)
mean(bottleneck_other$distance,na.rm=T)
mean(bottleneck_inter$distance,na.rm=T)
mean(TRN$distance,na.rm=T)


wilcox.test(bottleneck_bottleneck$distance,bottleneck$distance)
wilcox.test(bottleneck_other$distance,bottleneck$distance,alternative = "less")
wilcox.test(bottleneck_inter$distance,bottleneck$distance,alternative = "greater")

length(bottleneck_bottleneck$distance)
length(bottleneck_other$distance)
length(bottleneck_inter$distance)
length(TRN$distance)

plot(density(TRN$distance,na.rm=T),lty=1,xlab="distance",lwd=2)
lines(density(bottleneck_other$distance,na.rm=T),lty=2,lwd=2)
lines(density(bottleneck_inter$distance,na.rm=T),lty=3,lwd=2)
lines(density(TRN$distance,na.rm=T),lty=4,lwd=2)
legend("topright",c("+","-","+/-"),lty=c(1,2,3))