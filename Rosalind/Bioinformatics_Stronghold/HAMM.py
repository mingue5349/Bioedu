import sys

file_name = sys.argv[1]

with open(file_name,'r') as handle:
    cnt = 0
    seq1 = handle.readline().strip()
    seq2 = handle.readline().strip()
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            cnt += 1

print (cnt)