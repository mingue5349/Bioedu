import sys

file_name = sys.argv[1]
d = {}
with open(file_name, 'r') as handle:
    linelist = handle.readlines()
    for i in linelist:
        if '>' in i:
            header = i.replace('>','').strip()
            d[header] = ""
        else:
            d[header] += i.strip()

MaxGC_d = {}
for i in d.keys():
    GCper = 100*(d[i].count("G") + d[i].count("C"))/len(d[i])
    MaxGC_d[GCper] = i

MaxGC = max(MaxGC_d.keys())

print(MaxGC_d[MaxGC])
print(MaxGC)
