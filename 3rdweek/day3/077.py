import sys

file_name = sys.argv[1]

with open(file_name, 'r') as handle:
    linelist = []
    linedic = {}
    i = 0
    for line in handle:
        linelist = line.split('\t') 
        ch = linelist[0]
        start = linelist[1]
        end = linelist[2]
        BEDlength = int(end) - int(start) + 1
        i += BEDlength
        linedic[ch] = i

print (linedic)
        
