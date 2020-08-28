#!/usr/bin/env python3

import sys

f1 = open(sys.argv[1], 'r') 
f2 = open(sys.argv[2], 'r') 
f3 = open(sys.argv[3], 'r') 
f4 = open(sys.argv[4], 'r') 
f5 = open(sys.argv[5], 'r') 
f6 = open(sys.argv[6], 'r') 
f7 = open(sys.argv[7], 'w')

f7.write('ID\tRoot-Control-6h\tRoot-Control-12h\tRoot-Control-24h\tRoot-PA01-6h\tRoot-PA01-12h\tRoot-PA01-24h\n')

f1list = []
f2list = []
f3list = []
f4list = []
f5list = []
f6list = []

ID = set()

for f1line in f1:
  f1list.append(f1line.split('\t'))
for f2line in f2:
  f2list.append(f2line.split('\t'))
for f3line in f3:
  f3list.append(f3line.split('\t'))
for f4line in f4:
  f4list.append(f4line.split('\t'))
for f5line in f5:
  f5list.append(f5line.split('\t'))
for f6line in f6:
  f6list.append(f6line.split('\t'))

ID.add(f1list[0])
ID.add(f2list[0])
ID.add(f3list[0])
ID.add(f4list[0])
ID.add(f5list[0])
ID.add(f6list[0])

IDlist = list(ID)

for i in IDlist:
    f7.write(i + '\t')
    if i in f1list:
        f7.write(f1list[int(f1list.index(i)) + 1] + '\t')
    else:
        f7.write('\t')
    if i in f2list:
        f7.write(f2list[int(f2list.index(i)) + 1] + '\t')
    else:
        f7.write('\t')
    if i in f3list:
        f7.write(f3list[int(f3list.index(i)) + 1] + '\t')
    else:
        f7.write('\t')
    if i in f4list:
        f7.write(f4list[int(f4list.index(i)) + 1] + '\t')
    else:
        f7.write('\t')
    if i in f5list:
        f7.write(f5list[int(f5list.index(i)) + 1] + '\t')
    else:
        f7.write('\t')
    if i in f6list:
        f7.write(f6list[int(f6list.index(i)) + 1] + '\n')
    else:
        f7.write('\n')


