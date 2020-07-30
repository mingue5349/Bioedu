# QC visualization
/BiO/Install/FastQC_0.10.1/fastqc -t 4 --nogroup SRR1533626_1.temp.fq SRR1533626_2.temp.fq

# Trimming low quality reads
java -jar /BiO/Install/Trimmomatic-0.38/trimmomatic-0.38.jar PE -threads 4 -phred33 SRR1533626_1.temp.fq SRR1533626_2.temp.fq SRR1533626_1.trim.fq SRR1533626_1.unpair.fq SRR1533626_2.trim.fq SRR1533626_2.unpair.fq ILLUMINACLIP:/BiO/Install/Trimmomatic-0.38/adapters/TruSeq3-PE-2.fa:2:151:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36

# QC rechecking of trimmed reads
/BiO/Install/FastQC_0.10.1/fastqc -t 4 --nogroup SRR1533626_1.trim.fq SRR1533626_2.trim.fq

# BWA mapping
bwa mem -t 4 -R '@RG\tPL:Illumina\tID:Mingue\tSM:SRR1533626\tLB:HiSeq' /BiO/Education/WGS/REF/hg19.fa SRR1533626_1.trim.fq SRR1533626_2.trim.fq > SRR1533626.sam

# Duplication tagging
java -jar /BiO/Install/picard-tools-2.22.3/picard.jar AddOrReplaceReadGroups TMP_DIR=TEMP_PICARD VALIDATION_STRINGENCY=LENIENT SO=coordinate I=SRR1533626.sam O=SRR1533626_sorted.bam RGID=SRR1533626 RGLB=HiSeq RGPL=Illumina RGPU=unit RGSM=SRR1533626 CREATE_INDEX=true

# Remove duplicates
java -jar /BiO/Install/picard-tools-2.22.3/picard.jar MarkDuplicates TMP_DIR=TEMP_PICARD VALIDATION_STRINGENCY=LENIENT I=SRR1533626_sorted.bam O=SRR1533626_dedup.sam M=SRR1533626.duplicates_metrices REMOVE_DUPLICATES=true AS=true

# sorting. SAM --> BAM?
java -jar /BiO/Install/picard-tools-2.22.3/picard.jar SortSam TMP_DIR=TEMP_PICARD VALIDATION_STRINGENCY=LENIENT SO=coordinate I=SRR1533626_dedup.sam O=SRR1533626_dedup.bam CREATE_INDEX=true

# Finding base quality recalibrating region. (Add genome references)
java -Xmx8g -jar /BiO/Install/gatk-4.1.7.0/gatk-package-4.1.7.0-local.jar BaseRecalibrator -R /BiO/Education/WGS/REF/hg19.fa -I SRR1533626_dedup.bam --known-sites /BiO/Education/WGS/REF/dbsnp_138.hg19.vcf --known-sites /BiO/Education/WGS/REF/1000GENOMES-phase_3_indel.vcf -O SRR1533626_recal_pass1.table

# Applying recalibration to sequencing data
java -Xmx8g -jar /BiO/Install/gatk-4.1.7.0/gatk-package-4.1.7.0-local.jar ApplyBQSR -R /BiO/Education/WGS/REF/hg19.fa -I SRR1533626_dedup.bam --bqsr-recal-file SRR1533626_recal_pass1.table -O SRR1533626_recal_pass1.bam

# BQSR - 2nd pass
java -Xmx8g -jar /BiO/Install/gatk-4.1.7.0/gatk-package-4.1.7.0-local.jar BaseRecalibrator -R /BiO/Education/WGS/REF/hg19.fa -I SRR1533626_recal_pass1.bam --known-sites /BiO/Education/WGS/REF/dbsnp_138.hg19.vcf --known-sites /BiO/Education/WGS/REF/1000GENOMES-phase_3_indel.vcf -O SRR1533626_recal_pass2.table

# Apply recalibration - 2nd pass
java -Xmx8g -jar /BiO/Install/gatk-4.1.7.0/gatk-package-4.1.7.0-local.jar ApplyBQSR -R /BiO/Education/WGS/REF/hg19.fa -I SRR1533626_recal_pass1.bam -bqsr SRR1533626_recal_pass2.table -O SRR1533626_recal_pass2.bam

# Variant calling with HaplotypeCaller
java -Xmx8g -jar /BiO/Install/gatk-4.1.7.0/gatk-package-4.1.7.0-local.jar HaplotypeCaller -R /BiO/Education/WGS/REF/hg19.fa -I SRR1533626_recal_pass2.bam -O SRR1533626.rawVariants.g.vcf -ERC GVCF --standard-min-confidence-threshold-for-calling 20

# Merging gVCF results (SRR1002940 + SRR1533626)
java -Xmx8g -jar /BiO/Install/gatk-4.1.7.0/gatk-package-4.1.7.0-local.jar CombineGVCFs -R /BiO/Access/home/hykim/YUHS/REF/hg19.fa --variant SRR1002940.rawVariants.g.vcf --variant ../WGS_practice/SRR1533626.rawVariants.g.vcf -O cohort.g.vcf

# Applying GenotypeGVCFs
java -Xmx8g -jar /BiO/Install/gatk-4.1.7.0/gatk-package-4.1.7.0-local.jar GenotypeGVCFs -R /BiO/Education/WGS/REF/hg19.fa -V cohort.g.vcf -O cohort_genotype.vcf

# Extracting SNPs
java -Xmx8g -jar /BiO/Install/gatk-4.1.7.0/gatk-package-4.1.7.0-local.jar SelectVariants -R /BiO/Education/WGS/REF/hg19.fa -V cohort_genotype.vcf --select-type-to-include SNP -O cohort.rawSNPs.vcf

# Extracting INDELs
java -Xmx8g -jar /BiO/Install/gatk-4.1.7.0/gatk-package-4.1.7.0-local.jar SelectVariants -R /BiO/Education/WGS/REF/hg19.fa -V cohort_genotype.vcf --select-type-to-include INDEL -O cohort.rawINDELs.vcf

# Filtering SNPs
java -Xmx8g -jar /BiO/Install/gatk-4.1.7.0/gatk-package-4.1.7.0-local.jar VariantFiltration -R /BiO/Education/WGS/REF/hg19.fa -V cohort.rawSNPs.vcf -O cohort.rawSNPs.filtered.vcf --filter-name "." --filter-expression "QD < 2.0 || FS > 60.0 MQ < 40.0 || HaplotypeScore > 13.0 || MappingQualityRankSum < -12.5 || ReadPosRankSum < -8.0"

# Filtering INDELs
java -Xmx8g -jar /BiO/Install/gatk-4.1.7.0/gatk-package-4.1.7.0-local.jar VariantFiltration -R /BiO/Education/WGS/REF/hg19.fa -V cohort.rawINDELs.vcf -O cohort.rawINDELs.filtered.vcf --filter-name "." --filter-expression "QD < 2.0 || FS > 200.0 || ReadPosRankSum < -20.0"

# SortVcf
java -Xmx8g -jar /BiO/Install/gatk-4.1.7.0/gatk-package-4.1.7.0-local.jar SortVcf -I cohort.rawSNPs.filtered.vcf -I cohort.rawINDELs.filtered.vcf -O cohort.Filtered.variant.vcf

# MergeVcfs
java -Xmx8g -jar /BiO/Install/picard-tools-2.22.3/picard.jar MergeVcfs I= cohort.rawSNPs.filtered.vcf I= cohort.rawINDELs.filtered.vcf O= cohort.Filtered.variant.vcf

# Add Annotation
egrep "^#|PASS" cohort.Filtered.variant.vcf > cohort.Filtered.variant.PASS.vcf
perl /BiO/Install/annovar/table_annovar.pl cohort.Filtered.variant.PASS.vcf /BiO/Education/WGS/humandb/ -buildver hg19 -out cohort -remove -protocol refGene,cytoBand,avsnp138,clinvar_20190305 -operation g,r,f,f -nastring . -vcfinput

# Functional annotation with snpEff
java -jar /BiO/Access/home/hykim/YUHS/DATA2/snpEff/snpEff.jar -v hg19 cohort.Filtered.variant.PASS.vcf > cohort.snpEff.vcf

# SnpSift Annotate (dbSNP)
java -jar /BiO/Access/home/hykim/YUHS/DATA2/snpEff/SnpSift.jar annotate /BiO/Access/home/hykim/YUHS/REF/dbsnp_138.hg19.vcf cohort.snpEff.vcf > cohort.SnpEff.dbSNP138.vcf
