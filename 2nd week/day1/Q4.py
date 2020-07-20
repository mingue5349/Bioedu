#!/usr/bin/env python

seq = "AAAACCCGGT"

comp = {"A":"T", "T":"A", "C":"G", "G":"C"}

revseq = comp[seq[-1]]

print (revseq)
