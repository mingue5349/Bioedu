#!/usr/bin/python

import os

li = [6, 12, 24]

for i in li:
    os.system ("trimmomatic PE -threads 4 -summary 01.Clean/con/Shoot-Control-{0}h.trimmomatic.log 01.Clean/con/Shoot-Control-{0}h_1.nonadapt.fq.gz 01.Clean/con/Shoot-Control-{0}h_2.nonadapt.fq.gz 01.Clean/con/Shoot-Control-{0}h_R1.qt.P.fastq.gz 01.Clean/con/Shoot-Control-{0}h_R1.qt.U.fastq.gz 01.Clean/con/Shoot-Control-{0}h_R2.qt.P.fastq.gz 01.Clean/con/Shoot-Control-{0}h_R2.qt.U.fastq.gz SLIDINGWINDOW:4:20 MINLEN:50".format(i))

for i in li:
    os.system ("trimmomatic PE -threads 4 -summary 01.Clean/exp/Shoot-PA01-{0}h.trimmomatic.log 01.Clean/exp/Shoot-PA01-{0}h_1.nonadapt.fq.gz 01.Clean/exp/Shoot-PA01-{0}h_2.nonadapt.fq.gz 01.Clean/exp/Shoot-PA01-{0}h_R1.qt.P.fastq.gz 01.Clean/exp/Shoot-PA01-{0}h_R1.qt.U.fastq.gz 01.Clean/exp/Shoot-PA01-{0}h_R2.qt.P.fastq.gz 01.Clean/exp/Shoot-PA01-{0}h_R2.qt.U.fastq.gz SLIDINGWINDOW:4:20 MINLEN:50".format(i))
