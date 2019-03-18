# ------------------------ Analyze the features ------------------------------


setwd("/Users/dongqing/Desktop/Yeast/")
TRN <- read.table("4-Centrality/Data/TRN_dist.txt",header = TRUE,sep = "\t")
inhub <- read.table("4-Centrality/Result/inhub_all_296.txt",header = TRUE,sep = '\t')
inhub_inhub <- subset(inhub, type == "inhub",select = c("type","distance" ))
inhub_others <- subset(inhub, type == "others",select = c("type","distance" ))
inhub_inter <- subset(inhub, type == "inter",select = c("type","distance" ))


mean(inhub_inhub$distance,na.rm=T)
mean(inhub_others$distance,na.rm=T)
mean(inhub_inter$distance,na.rm=T)
mean(inhub$distance,na.rm=T)


wilcox.test(inhub_inhub$distance,inhub$distance,alternative='less')
wilcox.test(inhub_others$distance,inhub$distance,alternative='greater')
wilcox.test(inhub_inter$distance,inhub$distance,alternative='less')

length(inhub_inhub$distance)
length(inhub_others$distance)
length(inhub_inter$distance)
length(inhub$distance)

plot(density(inhub_inhub$distance,na.rm=T),lty=1,xlab="distance",lwd=2)
lines(density(inhub_others$distance,na.rm=T),lty=2,lwd=2)
lines(density(inhub_inter$distance,na.rm=T),lty=3,lwd=2)
lines(density(TRN$distance,na.rm=T),lty=4,lwd=2)
legend("topright",c("+","-","+/-"),lty=c(1,2,3))