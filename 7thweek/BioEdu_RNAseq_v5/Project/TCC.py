#!/usr/bin/python

import os

li = [6, 12, 24]

for i in li:
    os.system("samtools sort -n 02.Align/con/Shoot-Control-{0}h/accepted_hits.bam -o 02.Align/con/Shoot-Control-{0}h/accepted_hits.nameSorted.bam".format(i))
    os.system("htseq-count -f bam -r name -s no -m intersection-strict -o 02.Align/con/Shoot-Control-{0}h/accepted_hits.nameSorted.bam.SAMOUT 02.Align/con/Shoot-Control-{0}h/accepted_hits.nameSorted.bam BioResource/GeneModel/Arabidopsis_thaliana.TAIR10.44.gtf > 03.TCC/Shoot-Control-{0}h.count".format(i))

for i in li:
    os.system("samtools sort -n 02.Align/exp/Shoot-PA01-{0}h/accepted_hits.bam -o 02.Align/exp/Shoot-PA01-{0}h/accepted_hits.nameSorted.bam".format(i))
    os.system("htseq-count -f bam -r name -s no -m intersection-strict -o 02.Align/exp/Shoot-PA01-{0}h/accepted_hits.nameSorted.bam.SAMOUT 02.Align/exp/Shoot-PA01-{0}h/accepted_hits.nameSorted.bam BioResource/GeneModel/Arabidopsis_thaliana.TAIR10.44.gtf > 03.TCC/Shoot-PA01-{0}h.count".format(i))



