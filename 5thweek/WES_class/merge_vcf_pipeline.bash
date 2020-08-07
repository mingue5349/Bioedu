#!/bin/bash

# merging VCF (merged vcf data produced by me)
java -jar /BiO/apps/GenomeAnalysisTK-3.5/GenomeAnalysisTK.jar -T CombineVariants -R /BiO/data/reference/hg19.fasta -V ../NA12878/NA12878.consensus.filt.vcf -V ../NA12891/NA12891.consensus.filt.vcf -V ../NA12892/NA12892.consensus.filt.vcf | bgzip > WES.combined.vcf.gz

# filtering merged VCF
java -Xmx4g -jar /BiO/apps/snpEff/SnpSift.jar filter 'DP>60' WES.vcf.gz | bgzip > WES.filt.vcf.gz

# Annotating merged VCF (Snpeff)
java -Xmx4g -jar /BiO/apps/snpEff/snpEff.jar -lof -s WES_summary.html hg19 WES.filt.vcf.gz | bgzip > WES.snpeff.vcf.gz

# Annotating merged VCF (dbSNP)
java -Xmx4g -jar /BiO/apps/snpEff/SnpSift.jar annotate /BiO/data/DB/dbSnp151_chr.vcf.gz WES.snpeff.vcf.gz | bgzip > WES.snpeff.dbSnp151.vcf.gz

# Annotating merged VCF (clinvar)
java -Xmx4g -jar /BiO/apps/snpEff/SnpSift.jar annotate /BiO/data/DB/clinvar_20200728.vcf.gz WES.snpeff.dbSnp151.vcf.gz | bgzip > WES.snpeff.dbSnp151.clinvar.vcf.gz

# Annotating merged VCF (dbNSFP)
java -Xmx4g -jar /BiO/apps/snpEff/SnpSift.jar dbnsfp -db /BiO/data/DB/dbNSFP2.9.3.txt.gz WES.snpeff.dbSnp151.clinvar.vcf.gz | bgzip > WES.snpeff.dbSnp151.clinvar.dbnsfp.vcf.gz

# SnpSift extractFields
java -jar /BiO/apps/snpEff/SnpSift.jar extractFields -s ',' -e '.' WES.snpeff.dbSnp151.clinvar.dbnsfp.vcf.gz CHROM POS ID REF ALT GEN[0].GT GEN[1].GT GEN[2].GT GEN[0].AD GEN[1].AD GEN[2].AD ANN[*].GENE ANN[*].FEATUREID ANN[*].FEATURE ANN[*].BIOTYPE ANN[*].EFFECT ANN[*].IMPACT ANN[*].HGVS_C ANN[*].HGVS_P ANN[*].ERRORS CLNSIG dbNSFP_SIFT_pred > WES.table.txt





