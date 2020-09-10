#!/usr/bin/python

import os

os.system("cuffnorm --output-dir 06.Cuffnorm --labels Control,Experiment --num-threads 4 --library-type fr-unstranded --library-norm-method classic-fpkm --output-format simple-table BioResource/GeneModel/Arabidopsis_thaliana.TAIR10.44.gtf 05.Cuffquant/con/Shoot-Control-6h/abundances.cxb,05.Cuffquant/con/Shoot-Control-12h/abundances.cxb,05.Cuffquant/con/Shoot-Control-24h/abundances.cxb 05.Cuffquant/exp/Shoot-PA01-6h/abundances.cxb,05.Cuffquant/exp/Shoot-PA01-12h/abundances.cxb,05.Cuffquant/exp/Shoot-PA01-24h/abundances.cxb")
