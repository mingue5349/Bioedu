#!/usr/bin/python3

f1 = open('read_sample.txt', 'r')

print (f1.read().strip())

f1.close()


# 다른 방법

with open('read_sample.txt', 'r') as handle: #이렇게 하면 파일.close() 안해도 됨.
    for line in handle:
        if line.startswith(">"): #header 는 날리기
            continue
        print (line.strip())
