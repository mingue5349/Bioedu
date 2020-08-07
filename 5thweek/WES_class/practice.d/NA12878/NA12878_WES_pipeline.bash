#!/bin/bash

sample=$1 #(Do not write blank bewteen words)

# FASTQ trimming
#/BiO/apps/sickle/sickle pe -t sanger -g -f ${sample}_1.fastq.gz -r ${sample}_2.fastq.gz -o ${sample}-trimmed_1.fastq.gz -p ${sample}-trimmed_2.fastq.gz -s ${sample}-trimmed_3.fastq.gz

# FASTQ QC check
#/BiO/Install/FastQC_0.10.1/fastqc -t 4 --nogroup ${sample}-trimmed_*

# Alignment & BAM sorting. used partial reference (hg19_partial.fasta)
#/BiO/apps/bwa-0.7.17/bwa mem -t 4 -M -R "@RG\tID:BioEdu\tSM:${sample}\tPL:illumina\tLB:WES" /BiO/data/reference/hg19_partial.fasta ${sample}-trimmed_1.fastq.gz ${sample}-trimmed_2.fastq.gz | /BiO/apps/samtools/samtools view -bS -q 20 - | /BiO/apps/samtools/samtools sort -m 4000000000 -o ${sample}.sorted.bam

#############################################################
#############################################################

# copied new rmdup.bam file because of header error in hg19reference
cp /BiO/data/example/${sample}.sorted.bam . 

# Remove duplicates with MarkDuplicates
java -Xmx4g -jar /BiO/apps/gatk-4.1.2.0/gatk-package-4.1.2.0-local.jar MarkDuplicates -I ${sample}.sorted.bam -O ${sample}.rmdup.bam -M ${sample}.rmdup.metrices --REMOVE_DUPLICATES=true

# make bam index file
/BiO/apps/samtools/samtools index ${sample}.rmdup.bam 

# Base Quality Score Recalibration
java -Xmx4g -jar /BiO/apps/gatk-4.1.2.0/gatk-package-4.1.2.0-local.jar BaseRecalibrator -R /BiO/data/reference/hg19.fasta -I ${sample}.rmdup.bam -L /BiO/data/target/target.bed --known-sites /BiO/data/DB/dbSnp151_chr.vcf.gz --known-sites /BiO/data/DB/Mills_and_1000G_gold_standard.indels.hg19.vcf.gz -O ${sample}_recal_data.table

# Apply BQSR
java -Xmx4g -jar /BiO/apps/gatk-4.1.2.0/gatk-package-4.1.2.0-local.jar ApplyBQSR -bqsr ${sample}_recal_data.table -I ${sample}.rmdup.bam -O ${sample}.recal.bam

# make BQSR bam index file
/BiO/apps/samtools/samtools index ${sample}.recal.bam

# Find on-target reads
java -Xmx4g -jar /BiO/apps/GenomeAnalysisTK-3.5/GenomeAnalysisTK.jar -T DepthOfCoverage -R /BiO/data/reference/hg19.fasta -I ${sample}.recal.bam -o ${sample}_target_cov -ct 1 -ct 5 -ct 10 -ct 20 -ct 30 -omitBaseOutput -L /BiO/data/target/target.bed

# remove off target reads
bedtools intersect -wa -a ${sample}.recal.bam -b /BiO/data/target/target.bed > ${sample}.target.bam

# indexing targeted bam file
/BiO/apps/samtools/samtools index ${sample}.target.bam

# Variant calling - HaplotypeCaller
java -Xmx4g -jar /BiO/apps/gatk-4.1.2.0/gatk-package-4.1.2.0-local.jar HaplotypeCaller -R /BiO/data/reference/hg19.fasta -I ${sample}.target.bam -O ${sample}.gatk.vcf

# make vcf zip file
bgzip ${sample}.gatk.vcf

# make vcf index file
tabix -p vcf ${sample}.gatk.vcf.gz

# variant calling - samtools
/BiO/apps/bcftools/bcftools mpileup -f /BiO/data/reference/hg19.fasta ${sample}.target.bam | /BiO/apps/bcftools/bcftools call -mv -Ov -o ${sample}.samt.vcf

# make vcf zip file
bgzip ${sample}.samt.vcf

# make vcf index file
tabix -p vcf ${sample}.samt.vcf.gz

# make consensus vcf file (samtools + HaplotypeCaller)
vcf-isec -o -n +2 ${sample}.gatk.vcf.gz ${sample}.samt.vcf.gz > ${sample}.consensus.vcf

# Add tag to filtered vcf data
java -jar /BiO/apps/gatk-4.1.2.0/gatk-package-4.1.2.0-local.jar VariantFiltration -R /BiO/data/reference/hg19.fasta -O ${sample}.consensus.filt.vcf --variant ${sample}.consensus.vcf --filter-expression 'DP < 10 || FS > 60.0' --filter-name 'LOWQUAL'

# make final vcf with deleting 'LOWQUAL' variant data
cat ${sample}.consensus.filt.vcf | awk -F '\t' '($7!="LOWQUAL") {print}' | bgzip > ${sample}.final.vcf.gz

# make final vcf index file
tabix -p vcf ${sample}.final.vcf.gz












