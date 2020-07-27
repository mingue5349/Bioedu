import random
import sys

a = sys.argv[1]
b = sys.argv[2]

NTD_l = ['A', 'T', 'G', 'C']

def make_random_fa(a, b):
    with open('random_seq', 'w') as handle:
        for i in range(int(a)):
            handle.write('>Random_Seq_{0}\n'.format(i))
            randomseq = ""
            for j in range (int(b)):
                randomseq += random.choice(NTD_l)
            handle.write(randomseq + '\n')

make_random_fa(a, b)

with open('random_seq', 'r') as handle:
    d = {}
    for line in handle:
        if line.startswith('>'):
            print (line.strip() + ' ')
        else:
            for i in range(len(line)):
                if line[i] in d:
                    d[line[i].strip()] += 1
                else:
                    d[line[i].strip()] = 1
        print (d)
        d = {}
