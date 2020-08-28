#!/usr/bin/env python3

f1 = open('06.Cuffnorm/genes.fpkm_table', 'r')
f2 = open('04.Cuffmerge/merged.gtf','r')
f3 = open('06.Cuffnorm/genes.fpkm_table.ex', 'w')

#for f1line in f1:
#    f1line_l = f1line.split('\t')
#    for f2line in f2:
#        if f1line_l[0].strip() in f2line:
#            print('yes') # 여기서 맞는거 없음
#            f2line_l = f2line.split('\t')
#            f2id = f2line_l[8].split('"')
#            oId = f2id[9]
#            nearest_ref = f2id[11]
#            if oId.startswith('CUFF'):
#                f3.write(nearest_ref + '\t')
#            else:
#                f3.write(oId + '\t')
#            for i in range(1,len(f1line_l)-1):
#                f3.write(f1line_l[i] + '\t')
#            f3.write(f1line_l[-1] + '\t')

for f2line in f2:
    f2line_l = f2line.split('\t')
    f2_ID = f2line_l[8]
    ID_l = []
    for i in f2_ID:
        if 'gene_id' in i:
            ID_l.append(i.split(' ')[1])
        if 'oId' in i:
            ID_l.append
            




f1.close()
f2.close()
f3.close()

                
