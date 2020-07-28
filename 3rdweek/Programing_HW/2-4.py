import json
import sys

file_name = sys.argv[1]

def convert_from_json(file_name):
    with open(file_name, 'r') as handle:
        json_read = handle.read()
        dict = json.loads(json_read)
        return dict

def convert_to_json(file_name):
    with open(file_name, 'r') as handle:
        d = {}
        header = []
        content = []
        for line in handle:
            line_split = line.split(' ')  # input file 이 '\t' 가 ' ' 로 대체되어 ' ' 로 구분함.
            if '#' in line:
                header = line.split(' ')
                header[0].replace('#','')
            else:
                content = line.split(' ')
                for i in range(len(content)):
                    d[header[i].strip()] = content[i].strip()
        return json.dumps(d, indent=4)

print (convert_to_json(file_name))

