
# volcano plot

deg_table <- read.table("genes.deg.clean.tsv", header = T)
deg_up <- subset(deg_table, ISDEG=="YES" & UPDOWN=="UP")
deg_dw <- subset(deg_table, ISDEG=="YES" & UPDOWN=="DOWN")

plot(deg_table$M, -log(deg_table$P,10), cex=0.3, 
     ylim=c(0,50), xlim=c(-10,10))
points(deg_up$M, -log(deg_up$P,10), cex=0.3, col=2)
points(deg_dw$M, -log(deg_dw$P,10), cex=0.3, col=4)

# MA plot

deg_table <- read.table("genes.deg.clean.tsv", header = T)
deg_up <- subset(deg_table, ISDEG=="YES" & UPDOWN=="UP")
deg_dw <- subset(deg_table, ISDEG=="YES" & UPDOWN=="DOWN")

plot(deg_table$A, deg_table$M, cex=0.3,
     ylim=c(-10,10))
points(deg_up$A, deg_up$M, cex=0.3, col=2)
points(deg_dw$A, deg_dw$M, cex=0.3, col=4)

