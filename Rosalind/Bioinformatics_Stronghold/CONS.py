import sys

file_name = sys.argv[1]
d = {}
with open(file_name,'r') as handle:
    for line in handle:
        if '>' in line:
            d[line.strip()] = handle.readline().strip()

for i in d.values():

