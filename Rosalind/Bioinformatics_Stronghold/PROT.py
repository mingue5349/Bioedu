import sys

seq_file = sys.argv[1]
RNATable = sys.argv[2]

with open(seq_file,'r') as handle:
    seq = handle.readline()

trans_d = {}
trans_l = []
with open(RNATable,'r') as handle:
    for line in handle:
        trans_l = line.split(" ")
        for i in range(len(trans_l)):
            if len(trans_l[i]) == 3:
                trans_d[trans_l[i]] = trans_l[i+1].strip()

for i in range(0, len(seq),3):
    amino_acid = seq[i:i+3]
    print (trans_d[amino_acid], end= "")
print ()