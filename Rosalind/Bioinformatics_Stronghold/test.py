#!/usr/bin/env python

n, k = 5, 3

g1, g2 = 1, 1

for m in range (1, 5-1):
    g3 = g1 + g2*k
    g2 = g1
    g1 = g3
print (g1)
