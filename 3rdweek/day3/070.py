cnt = 0
deletion = 0
insertion = 0

with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("#"):
            continue
        splitted = line.split('\t')
        chrom = splitted[0]
        pos = splitted[1]
        id_ = splitted[2]
        ref = splitted[3]
        alt_ = splitted[4]
        alts = splitted[4].split(",")
        if len(ref) != len(alts):
            for alt in alts:
                if len(ref)>len(alt):
                    deletion += 1
                if len(ref)<len(alt):
                    insertion += 1
        if len(ref) == len(alts):
            if len(ref)>len(alt_):
                deletion + 1
            elif len(ref)<len(alt_):
                insertion + 1

print ("ins:" +str(insertion))
print ("del:" +str(deletion))
