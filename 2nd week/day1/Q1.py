#!/usr/bin/env python

seq = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

numA = seq.count("A")
numT = seq.count("T")
numG = seq.count("G")
numC = seq.count("C")

print ("A : {0} T : {1} G : {2} C : {3}".format(numA,numT,numG,numC))
