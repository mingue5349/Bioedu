#!/usr/bin/python

import os

l1 = [12, 24]
l2 = [6, 12, 24]

#for i in l1:
#    os.system ("cutadapt -a AGATCGGAAGAGC -A AGATCGGAAGAGC -o 01.Clean/con/Shoot-Control-{0}h_1.nonadapt.fq.gz -p 01.Clean/con/Shoot-Control-{0}h_2.nonadapt.fq.gz 00.Rawdata/con/Shoot-Control-{0}h_1.fastq.gz 00.Rawdata/con/Shoot-Control-{0}h_2.fastq.gz".format(i))

for i in l2:
    os.system ("cutadapt -a AGATCGGAAGAGC -A AGATCGGAAGAGC -o 01.Clean/exp/Shoot-PA01-{0}h_1.nonadapt.fq.gz -p 01.Clean/exp/Shoot-PA01-{0}h_2.nonadapt.fq.gz 00.Rawdata/exp/Shoot-PA01-{0}h_1.fastq.gz 00.Rawdata/exp/Shoot-PA01-{0}h_2.fastq.gz".format(i))
