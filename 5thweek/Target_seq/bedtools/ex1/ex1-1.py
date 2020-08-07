#!/usr/bin/env python3

import operator
chr_d = {}

with open ("step1.bed", 'r') as handle:
	for line in handle:
		split_chr = line.split('\t')[0]
		if split_chr in chr_d.keys():
			chr_d[split_chr] += 1
		else:
			chr_d[split_chr] = 0

print (chr_d)
print (max(chr_d.items(), key=operator.itemgetter(1))[0])

