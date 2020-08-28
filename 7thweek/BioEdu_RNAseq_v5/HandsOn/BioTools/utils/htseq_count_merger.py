#!/usr/bin/python
# @seung1.yoo
# For RNAseq Edu
# Only Simple "def"

import os

def parse_infiles(infiles):
    infile_dic = dict()
    for infile in infiles:
        fbn = os.path.basename(infile)
        sn = fbn.rstrip('.count')
        infile_dic.setdefault(sn, infile)
    return infile_dic

def merge_count(infile_dic):
    count_dic = dict()
    for sn, infile in infile_dic.iteritems():
        print sn, infile
        for line in open(infile):
            if line.startswith('__'):
                print line.rstrip()
                continue
            items = line.rstrip('\n').split('\t')
            gid = items[0]
            count = items[1]
            count_dic.setdefault(gid, {}).setdefault(sn, count)
    return count_dic

def make_output(outprefix, outtype, count_dic, sns):
    out = open('{0}.{1}.mtx'.format(outprefix, outtype), 'w')
    out.write('ID\t{0}\n'.format('\t'.join(sns)))
    for gid, sn_dic in sorted(count_dic.iteritems()):
        units = [gid]
        for sn in sns:
            count = sn_dic[sn]
            units.append(count)
        out.write('{0}\n'.format('\t'.join([str(x) for x in units])))
    out.close()

def normalizer(count_dic):
    sum_dic = dict()
    for gid, sn_dic in sorted(count_dic.iteritems()):
        for sn, count in sn_dic.iteritems():
            sum_dic.setdefault(sn, 0)
            sum_dic[sn] += int(count)
    #
    # {(10^9 * Count) / TotalCount}
    norm_dic = dict()
    for gid, sn_dic in sorted(count_dic.iteritems()):
        for sn, count in sn_dic.iteritems():
            norm_val = round((10^9 * int(count)) / float(sum_dic[sn]),6)
            norm_dic.setdefault(gid, {}).setdefault(sn, norm_val)
    return norm_dic

def main(args):
    infile_dic = parse_infiles(args.infiles)
    sns = sorted(infile_dic.keys())
    count_dic = merge_count(infile_dic)
    norm_dic = normalizer(count_dic)
    #
    make_output(args.outprefix, 'raw', count_dic, sns)
    make_output(args.outprefix, 'norm', norm_dic, sns)

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Merge output of HTSeq-count")
    parser.add_argument('--infiles', nargs="+", help='file name must be [PATH]/[sample name].count')
    parser.add_argument('--outprefix')
    args = parser.parse_args()
    main(args)

