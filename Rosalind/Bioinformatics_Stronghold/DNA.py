#!/usr/bin/env python

DNA = 'TCTAGATGCACGCTCCTATGGATCGGCAATCGGAATTGCTCTTGATAATAATAGAATCTATACTTTTCTGCTTGTACCTTCAAGGACTCGTCATACACAGGCTCCACAAGACATCGCGTATCGAAAAGAGGCTGAATCCGGTACCCGGCGTAGCCCTCTTTGAGACGTCACTAAGCTATACGGCTGAGCTGCGGTGATCCGTGTTTTGTCATGGGCCACGATAAGCAACCCGAGCAGAGGGCATACAAACTGCTGCTTACCCTGACTGCAGCATTCGTGTGCTTATACGAGATCACATGTATATAACGATGAGTGGGACCAGCTATCGCGCTCTCGGACTCACTCATCCACATGATCTAGGGCCCTGAACAGGATAGTAGAGATTTTGTGGTTTCTTGCGCTGGACTCTTCTCCCTAATTCTTCGCCGCATCCTGAATACACAACGATAAGTTCATATGAGCGTAGTCCTGACTGTAGGTCCTCCAACCCTAATAGCTAAACTCCTGAGCCTTGACGCTTCACCATCCAAGCGCAGCGTTCCCCGCTGTTTGCTGGGCATATACTCTCTCCGTTAGCGCGTTCGCGCTAGCTTGGGCACGGTTAGTGGCTCTTAAAATCCCTGCCACACCACCTCAGGGCTCAAAGTTGGATTAGGCGATAGGTTACATGACAATACTCAATACTATGTTCTAGTAAATGGAGGACTGTGAGCGTGTCGCAATAAATGTGTCGACATACCAGGCTCATCGGTTCATCGGCGTGTCCTCTACAAACATCCGTATAACAATAACTAACATGGCG'

numA = DNA.count('A')
numT = DNA.count('T')
numG = DNA.count('G')
numC = DNA.count('C')

print (numA, numC, numG, numT)
