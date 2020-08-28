library(TCC)


raw_count <- read.table("03.TCC/count.raw.mtx", header = T, row.names = 1)
sel_col <- c(1,2,3,4,5,6)
group <- c(1,1,1,2,2,2)

## Set TCC
tcc <- new("TCC", raw_count, group)
dim(tcc$count)
tcc <- filterLowCountGenes(tcc)
dim(tcc$count)

## Differential Expressed Genes Analysis
type <- "edger"
#type <- "deseq"
## edgeR or DESeq
if (type == "edger"){
    tcc <- calcNormFactors(tcc, norm.method="tmm", test.method="edger",
                           iteration=3, FDR=0.1, floorPDEG=0.05)
    tcc <- estimateDE(tcc, test.method="edger", FDR=0.1)
}else if (type == "deseq"){
    tcc <- calcNormFactors(tcc, norm.method="deseq", test.method="deseq",
                           iteration=3, FDR=0.1, floorPDEG=0.05)
    tcc <- estimateDE(tcc, test.method="deseq", FDR=0.1)
}

table(tcc$estimatedDEG)

# The getNormalizedData function can be applied to the TCC class object after the normalization factors have been calculated
eff_count <- getNormalizedData(tcc)
write.table(round(eff_count,3), "03.TCC/count.tmm.mtx", sep="\t", quote=F, col.names=T, row.names=T)

# The summary statistics for top-ranked genes
result <- getResult(tcc, sort=TRUE)
write.table(result, "03.TCC/DEG.xls", sep="\t", quote=F, col.names=T, row.names=F)

# The plot function generates an M-A plot
# An MA-plot is a plot of log-fold change (M-values, i.e. the log of the ratio of level counts for each gene between two samples) against the log-average (A-values, i.e. the average level counts for each gene across the two samples).
# The MA-plot is a useful to visualize reproducibility between samples of an experiment. From a MA-plot one can see if normalization is needed.
# In MA plot, genes with similar expression levels in two samples will appear around the horizontal line y = 0. A lowess fit (in red) is plotted underlying a possible trend in the bias related to the mean expression.
png("03.TCC/DEG.MA.png", width=640, height = 640)
plot(tcc, median.lines = TRUE, cex=0.4)
dev.off()

