import sys
import json

file_name = sys.argv[1]

d = {}

with open (file_name, 'r') as handle:
    for line in handle:
        if '>' in line:
            continue
        else:
            for s in line.strip():
                if s in d:
                    d[s] += 1
                else:
                    d[s] = 1

print (json.dumps(d, indent=4))
