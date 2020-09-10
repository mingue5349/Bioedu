#!/usr/bin/python

import os

os.system("cuffdiff --output-dir 07.Cuffdiff --labels Control,Experiment --frag-bias-correct BioResource/Reference/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa --multi-read-correct --num-threads 4 --library-type fr-unstranded --library-norm-method classic-fpkm --dispersion-method pooled BioResource/GeneModel/Arabidopsis_thaliana.TAIR10.44.gtf 05.Cuffquant/con/Shoot-Control-6h/abundances.cxb,05.Cuffquant/con/Shoot-Control-12h/abundances.cxb,05.Cuffquant/con/Shoot-Control-24h/abundances.cxb 05.Cuffquant/exp/Shoot-PA01-6h/abundances.cxb,05.Cuffquant/exp/Shoot-PA01-12h/abundances.cxb,05.Cuffquant/exp/Shoot-PA01-24h/abundances.cxb")


