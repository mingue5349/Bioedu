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

# count NTD of each loci
NTD_no = []
for i in d.values():   # d.values() = sequences
    if len(NTD_no) == 0:
        for j in range(len(i)):
            NTD_no.append(i[j])
    else:
        for j in range(len(i)):
            NTD_no[j] += i[j]

concensus = ""
cnt_d = {}
Anum_l = []
Tnum_l = []
Gnum_l = []
Cnum_l = []

for i in NTD_no:
    cnt_d['A'] = i.count('A')
    Anum_l.append(i.count('A'))
    cnt_d['T'] = i.count('T')
    Tnum_l.append(i.count('T'))
    cnt_d['C'] = i.count('C')
    Cnum_l.append(i.count('C'))
    cnt_d['G'] = i.count('G')
    Gnum_l.append(i.count('G'))
    if cnt_d['A'] == max(cnt_d.values()):
        NTD = 'A'
    elif cnt_d['T'] == max(cnt_d.values()):
        NTD = 'T'
    elif cnt_d['G'] == max(cnt_d.values()):
        NTD = 'G'
    elif cnt_d['C'] == max(cnt_d.values()):
        NTD = 'C'
    concensus += NTD
    NTD = ""

with open('CONS.output.txt' ,'w') as handle:
    handle.write(concensus + '\n')
    handle.write('A: ')
    for i in Anum_l:
        handle.write(str(i) + ' ' )
    handle.write('\n')
    handle.write('C: ')
    for i in Cnum_l:
        handle.write(str(i) + ' ' )
    handle.write('\n')
    handle.write('G: ')
    for i in Gnum_l:
        handle.write(str(i) + ' ')
    handle.write('\n')
    handle.write('T: ')
    for i in Tnum_l:
        handle.write(str(i) + ' ')
    handle.write('\n')



