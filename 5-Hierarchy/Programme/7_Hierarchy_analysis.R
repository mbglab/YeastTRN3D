# ------------------------- Analyze the hierarchical features -------------------------

setwd("/Users/dongqing/Desktop/Yeast/")
hir_3d <- read.table("5-Hierarchy/Result/hir_3d.txt",header = TRUE,sep = "\t")

hir_3d$hier <- as.factor(paste(hir_3d$hier1,hir_3d$hier2,sep = "-"))
table(hir_3d$hier)

hir_3d_TM <- subset(hir_3d, hir_3d$hier == "Top-Middle",select = "distance")
hir_3d_TB <- subset(hir_3d, hir_3d$hier == "Top-Bottom",select = "distance")
hir_3d_TTG <- subset(hir_3d, hir_3d$hier == "Top-Target",select = "distance")
hir_3d_MM <- subset(hir_3d, hir_3d$hier == "Middle-Middle",select = "distance")
hir_3d_MB <- subset(hir_3d, hir_3d$hier == "Middle-Bottom",select = "distance")
hir_3d_MT <- subset(hir_3d, hir_3d$hier == "Middle-Target",select = "distance")
hir_3d_BTG <- subset(hir_3d, hir_3d$hier == "Bottom-Target",select = "distance")
hir_3d_BB <- subset(hir_3d, hir_3d$hier == "Bottom-Bottom",select = "distance")

mean(hir_3d_TM$distance,na.rm=T)
mean(hir_3d_TB$distance,na.rm=T)
mean(hir_3d_TTG$distance,na.rm=T)
mean(hir_3d_MM$distance,na.rm=T)
mean(hir_3d_MB$distance,na.rm=T)
mean(hir_3d_MT$distance,na.rm=T)
mean(hir_3d_BTG$distance,na.rm=T)
mean(hir_3d_BB$distance,na.rm=T)

wilcox.test(hir_3d_TM$distance,hir_3d$distance,alternative = "less")
wilcox.test(hir_3d_TB$distance,hir_3d$distance,alternative = "less")
wilcox.test(hir_3d_TTG$distance,hir_3d$distance,alternative = "less")
wilcox.test(hir_3d_MM$distance,hir_3d$distance)
wilcox.test(hir_3d_MB$distance,hir_3d$distance)
wilcox.test(hir_3d_MT$distance,hir_3d$distance,alternative = "greater")
wilcox.test(hir_3d_BTG$distance,hir_3d$distance)