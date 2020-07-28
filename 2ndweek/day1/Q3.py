#!/usr/bin/env python

seq = "AAAACCCGGT"

seq = seq.replace('A','t')
seq = seq.replace('C','g')
seq = seq.replace('G','c')
seq = seq.replace('T','a')

seq = seq.upper()

rev = seq[::-1]

print (rev)
