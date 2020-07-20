#!/usr/bin/env python

def add(a,b):
    print ('add', a, 'and', b)
    print ('%d + %d =' %(a,b), a+b)
    return a, b, a+b

result = add(3,4)
print ('result:', result)
print ('resultA:', result)
print ('resultB:', result)
print ('resultA+B:', result)

def hello():
    print ("Hello!")

hello()
