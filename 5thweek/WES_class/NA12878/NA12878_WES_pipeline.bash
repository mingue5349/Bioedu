#!/bin/bash

# FASTQ trimming
#/BiO/apps/sickle/sickle pe -t sanger -g -f NA12878_1.fastq.gz -r NA12878_2.fastq.gz -o NA12878-trimmed_1.fastq.gz -p NA12878-trimmed_2.fastq.gz -s NA12878-trimmed_3.fastq.gz

# FASTQ QC check
#/BiO/Install/FastQC_0.10.1/fastqc -t 4 --nogroup NA12878-trimmed_*

# Alignment & BAM sorting. used partial reference (hg19_partial.fasta)
#/BiO/apps/bwa-0.7.17/bwa mem -t 4 -M -R "@RG\tID:BioEdu\tSM:NA12878\tPL:illumina\tLB:WES" /BiO/data/reference/hg19_partial.fasta NA12878-trimmed_1.fastq.gz NA12878-trimmed_2.fastq.gz | /BiO/apps/samtools/samtools view -bS -q 20 - | /BiO/apps/samtools/samtools sort -m 4000000000 -o NA12878.sorted.bam

#############################################################
#############################################################

# copied new rmdup.bam file because of header error in hg19reference
cp /BiO/data/example/NA12878.sorted.bam . 

# Remove duplicates with MarkDuplicates
java -Xmx4g -jar /BiO/apps/gatk-4.1.2.0/gatk-package-4.1.2.0-local.jar MarkDuplicates -I NA12878.sorted.bam -O NA12878.rmdup.bam -M NA12878.rmdup.metrices --REMOVE_DUPLICATES=true

# make bam index file
/BiO/apps/samtools/samtools index NA12878.rmdup-cp.bam 

# Base Quality Score Recalibration
java -Xmx4g -jar /BiO/apps/gatk-4.1.2.0/gatk-package-4.1.2.0-local.jar BaseRecalibrator -R /BiO/data/reference/hg19.fasta -I NA12878.rmdup-cp.bam -L /BiO/data/target/target.bed --known-sites /BiO/data/DB/dbSnp151_chr.vcf.gz --known-sites /BiO/data/DB/Mills_and_1000G_gold_standard.indels.hg19.vcf.gz -O NA12878_recal_data-cp.table

# Apply BQSR
java -Xmx4g -jar /BiO/apps/gatk-4.1.2.0/gatk-package-4.1.2.0-local.jar ApplyBQSR -bqsr NA12878_recal_data.table -I NA12878.rmdup.bam -O NA12878.recal.bam

# make BQSR bam index file
/BiO/apps/samtools/samtools index NA12878.recal.bam

# Find on-target reads
java -Xmx4g -jar /BiO/apps/GenomeAnalysisTK-3.5/GenomeAnalysisTK.jar -T DepthOfCoverage -R /BiO/data/reference/hg19.fasta -I NA12878.recal.bam -o NA12878_target_cov -ct 1 -ct 5 -ct 10 -ct 20 -ct 30 -omitBaseOutput -L /BiO/data/target/target.bed

# remove off target reads
bedtools intersect -wa -a NA12878.recal-cp.bam -b /BiO/data/target/target.bed > NA12878.target.bam

# indexing targeted bam file
/BiO/apps/samtools/samtools index NA12878.target.bam

# Variant calling - HaplotypeCaller
java -Xmx4g -jar /BiO/apps/gatk-4.1.2.0/gatk-package-4.1.2.0-local.jar HaplotypeCaller -R /BiO/data/reference/hg19.fasta -I NA12878.target.bam -O NA12878.gatk.vcf

# make vcf zip file
bgzip NA12878.gatk.vcf

# make vcf index file
tabix -p vcf NA12878.gatk.vcf.gz

# variant calling - samtools
/BiO/apps/bcftools/bcftools mpileup -f /BiO/data/reference/hg19.fasta NA12878.target.bam | /BiO/apps/bcftools/bcftools call -mv -Ov -o NA12878.samt.vcf

# make vcf zip file
bgzip NA12878.samt.vcf

# make vcf index file
tabix -p vcf NA12878.samt.vcf.gz

# make consensus vcf file (samtools + HaplotypeCaller)
vcf-isec -o -n +2 NA12878.gatk.vcf.gz NA12878.samt.vcf.gz > NA12878.consensus.vcf

# Add tag to filtered vcf data
java -jar /BiO/apps/gatk-4.1.2.0/gatk-package-4.1.2.0-local.jar VariantFiltration -R /BiO/data/reference/hg19.fasta -O NA12878.consensus.filt.vcf --variant NA12878.consensus.vcf --filter-expression 'DP < 10 || FS > 60.0' --filter-name 'LOWQUAL'

# make final vcf with deleting 'LOWQUAL' variant data
cat NA12878.consensus.filt.vcf | awk -F '\t' '($7!="LOWQUAL") {print}' | bgzip > NA12878.final.vcf.gz

# make final vcf index file
tabix -p vcf NA12878.final.vcf.gz












