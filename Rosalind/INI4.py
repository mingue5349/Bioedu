#!/usr/bin/env python

int1 = int(input("input no.:"))
int2 = int(input("input no.:"))

li = []

for i in range(int1, int2):
    li.append(i)

for i in li:
    if i%2 == 0:
        li.remove(i)

print (sum(li))        
