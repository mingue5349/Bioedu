
#setwd()
rpkm_table <- read.table("genes.fpkm.tsv", header = T)
dim(rpkm_table)
head(rpkm_table, 3)
summary(rpkm_table)

# Histogram
log(0.0, 2)

rpkm_table$RootControl6h

hist(rpkm_table$RootControl6h, breaks = 10)
hist(log(rpkm_table$RootControl6h, 2), breaks = 10)
hist(log(rpkm_table$RootControl6h+1, 2), breaks = 10)
#hist(log(rpkm_table$RootControl6h+1, 2), breaks = 10, probability = T)

par(mfrow=c(1,3))
hist(rpkm_table$RootControl6h, breaks = 10)
hist(log(rpkm_table$RootControl6h, 2), breaks = 10)
hist(log(rpkm_table$RootControl6h+1, 2), breaks = 10)
par(mfrow=c(1,1))
hist(log(rpkm_table$RootControl6h+1, 2), breaks = 10, probability = T)

par(mfrow=c(2,3))
hist(log(rpkm_table$RootControl6h+1, 2), breaks = 10, probability = T)
hist(log(rpkm_table$RootControl12h+1, 2), breaks = 10, probability = T)
hist(log(rpkm_table$RootControl24h+1, 2), breaks = 10, probability = T)
hist(log(rpkm_table$RootPA016h+1, 2), breaks = 10, probability = T)
hist(log(rpkm_table$RootPA0112h+1, 2), breaks = 10, probability = T)
hist(log(rpkm_table$RootPA0124h+1, 2), breaks = 10, probability = T)
par(mfrow=c(1,1))

par(mfrow=c(2,3))
hist(log(rpkm_table$RootControl6h, 2), breaks = 10, probability = T)
hist(log(rpkm_table$RootControl12h, 2), breaks = 10, probability = T)
hist(log(rpkm_table$RootControl24h, 2), breaks = 10, probability = T)
hist(log(rpkm_table$RootPA016h, 2), breaks = 10, probability = T)
hist(log(rpkm_table$RootPA0112h, 2), breaks = 10, probability = T)
hist(log(rpkm_table$RootPA0124h, 2), breaks = 10, probability = T)
par(mfrow=c(1,1))


# Scatter plot
plot(rpkm_table$RootControl6h, rpkm_table$RootPA016h, col="red", pch =19)

par(mfrow=c(2,2))
plot(log(rpkm_table$RootControl6h+1, 2), log(rpkm_table$RootPA016h+1, 2), col="red", pch =19)
plot.new()
plot.new()
plot(log(rpkm_table$RootControl12h+1, 2), log(rpkm_table$RootPA0112h+1, 2), col="blue", pch =19)
par(mfrow=c(1,1))

# Box plot
boxplot(log(rpkm_table[,c(2:7)]+1, 2))

rpkm_table <- read.table("genes.fpkm.tsv", header = T)
rpkm_table <- rpkm_table[which(apply(rpkm_table[,c(2:7)],1,max)>=0.3),]
dim(rpkm_table)
head(rpkm_table, 3)
summary(rpkm_table)
boxplot(log(rpkm_table[,c(2:7)]+1, 2))

# MDS
rpkm_table <- read.table("genes.fpkm.tsv", header = T, row.names = 1)
t_rpkm_table <- t(rpkm_table)
group <- c(1,1,1,2,2,2)
d <- dist(log(t_rpkm_table+0.1,10), method="euclidean")
fit <- cmdscale(d, eig=TRUE, k=2)
x <- fit$points[,1]
y <- fit$points[,2]
plot(x, y, xlab="Coordinate 1", ylab="Coordinate 2", main="MDS", type="n")
text(x, y, labels=row.names(t_rpkm_table), cex=.7, col=group)
grid()

