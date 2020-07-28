import sys

file_name = sys.argv[1]

seq = ""
with open (file_name, 'r') as handle:
    line_l = handle.readlines()
    for i in line_l:
        if i.startswith('>'):
            continue
        else:
            i = i.strip()
            seq += i

seq.replace("A","t")
seq.replace("T","a")
seq.replace("G","c")
seq.replace("C","g")
seq = seq.upper()
print (seq[::-1])
