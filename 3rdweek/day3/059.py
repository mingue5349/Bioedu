# Biopython 의 SeqIO 를 사용해 FASTA 파일 파싱하기

from Bio import SeqIO

record = SeqIO.read("059.fasta", "fasta")

A = record.seq.count('A')
T = record.seq.count('T')
G = record.seq.count('G')
C = record.seq.count('C')

print (f"A: {A}") # A: 497
print (f"C: {C}") # C: 444
print (f"G: {G}") # G: 585
print (f"T: {T}") # T: 514


