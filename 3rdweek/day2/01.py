# -*- conding: utf-8 -*-
import sys
import gzip  # zip 파일 열기 위한 모듈

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [fasta.gz]")
    sys.exit()

f = sys.argv[1]

d = {}

# gzip 열기위해 gzip.open, rb = read binary
with gzip.open(f, 'rb') as handle:
    for line in handle:
        line = line.decode("utf-8")
        if line.startswith('>'):
            continue
        else:
            for s in line.strip():
                if s in d:
                    d[s] += 1
                else:
                    d[s] = 1

    for i in d.values():
        result = sum(d.values())

with open("result1.txt", 'w') as handle:
    handle.write(d)  # 이 부분 수정하기
    handle.write(result)
