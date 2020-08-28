
import sys

def iter_attr_s(attr_s):
	for _attr in attr_s:
		if not _attr:
			continue
		key = _attr.strip().split()[0]
		value = ' '.join(_attr.strip().split()[1:]).strip('"')
		yield key, value

def parse_mergedgtf(fn):
	id_dic = dict()
	for line in open(fn):
		items = line.rstrip('\n').split('\t')
		attr_s = items[-1].split(';')
		#
		xloc = ''
		oId = ''
		ref = ''
		for key, value in iter_attr_s(attr_s):
			if key in ['gene_id']:
				xloc = value
			elif key in ['oId']:
				oId = value.upper()
			elif key in ['nearest_ref']:
				ref = value.upper()
		#
		if xloc and oId:
			id_dic.setdefault(xloc, oId)
		elif xloc and ref:
			id_dic.setdefault(xloc, ref)
		else:
			print 'ERROR, Could not found. {0} {1}'.format(xloc, oId)
			sys.exit()

	return id_dic

def main(args):
	id_dic = parse_mergedgtf(args.mergedgtf)

	outfh = open(args.outfn, 'w')
	for line in open(args.infn):
		items = line.rstrip('\n').split('\t')
		if items[0] in ['tracking_id', 'test_id']:
			outfh.write(line)
			continue
		if items[0] in id_dic:
			new_items = [id_dic[items[0]]]
			new_items.extend(items[1:])
			outfh.write('{0}\n'.format('\t'.join(new_items)))
		else:
			print 'ERROR, Could not found. {0}'.format(items[0])
			sys.exit()
	outfh.close()
			


if __name__=='__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('infn')
	parser.add_argument('outfn')
	parser.add_argument('mergedgtf')
	args = parser.parse_args()
	main(args)
