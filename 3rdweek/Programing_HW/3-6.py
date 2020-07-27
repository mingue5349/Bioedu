with open('/mnt/c/Users/mingu/PycharmProjects/GB/Github/Bioedu/3rdweek/day3/070.vcf','r') as handle:

    alt_col = 0
    ref_col = 0
    alt_cnt = 0
    for line in handle:
        if line.startswith('#CHROM'):
            line_l = line.split('\t')
            for i in range(len(line_l)):
                if 'ALT' in line_l[i]:
                    alt_col = i
                elif 'REF' in line_l[i]:
                    ref_col = i
        elif '#' not in line:
            line_l2 = line.split('\t')
            alt_cnt += line_l2[alt_col].count(',') + 1

    print (alt_cnt)
