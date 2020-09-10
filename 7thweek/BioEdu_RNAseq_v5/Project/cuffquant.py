#!/usr/bin/python

import os

li = [6, 12, 24]


# con
for i in li:
    os.system("cuffquant --output-dir 05.Cuffquant/con/Shoot-Control-{0}h --frag-bias-correct BioResource/Reference/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa --multi-read-correct --num-threads 4 --library-type fr-unstranded -M BioResource/GeneModel/Arabidopsis_thaliana.TAIR10.44.mask.gtf BioResource/GeneModel/Arabidopsis_thaliana.TAIR10.44.gtf 02.Align/con/Shoot-Control-{0}h/accepted_hits.bam".format(i))

# exp

for i in li:
    os.system("cuffquant --output-dir 05.Cuffquant/exp/Shoot-PA01-{0}h --frag-bias-correct BioResource/Reference/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa --multi-read-correct --num-threads 4 --library-type fr-unstranded -M BioResource/GeneModel/Arabidopsis_thaliana.TAIR10.44.mask.gtf BioResource/GeneModel/Arabidopsis_thaliana.TAIR10.44.gtf 02.Align/exp/Shoot-PA01-{0}h/accepted_hits.bam".format(i))
