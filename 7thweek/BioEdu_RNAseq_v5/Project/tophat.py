#!/usr/bin/python

import os

li = [6, 12, 24]

for i in li:
    os.system("tophat -o 02.Align/con/Shoot-Control-{0}h -p 4 -r 250 --mate-std-dev 50 --library-type fr-unstranded -G BioResource/GeneModel/Arabidopsis_thaliana.TAIR10.44.gtf --rg-id control --rg-sample Shoot-Control-{0}h BioResource/Reference/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa 01.Clean/con/Shoot-Control-{0}h_R1.qt.P.fastq.gz 01.Clean/con/Shoot-Control-{0}h_R2.qt.P.fastq.gz".format(i))

for i in li:
    os.system("tophat -o 02.Align/exp/Shoot-PA01-{0}h -p 8 -r 250 --mate-std-dev 50 --library-type fr-unstranded -G BioResource/GeneModel/Arabidopsis_thaliana.TAIR10.44.gtf --rg-id experiment --rg-sample Shoot-PA01-{0}h BioResource/Reference/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa 01.Clean/exp/Shoot-PA01-{0}h_R1.qt.P.fastq.gz 01.Clean/exp/Shoot-PA01-{0}h_R2.qt.P.fastq.gz".format(i))

