with open('/mnt/c/Users/mingu/PycharmProjects/GB/Github/Bioedu/3rdweek/day3/070.vcf','r') as handle:
    for line in handle:
        if line.startswith('#CHROM'):
            line_l = line.split('\t')
            print (line_l[0:5])
        elif '#' not in line:
            line_l2 = line.split('\t')
            if 'rs' in line_l2[2]:
                print(line_l2[0:5])


