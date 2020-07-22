#!/usr/bin/env python

i_lambda = (lambda x, y: x + y)(3,4)

print (i_lambda)

def add(x, y):
    return (x + y)

print (add(3,4))




#def book(name, age, *book):
#    print (name, age, end = ' ')
#    for i in book:
#        print (i, end = ' ')
#    print ()
#    return name
#
#name1 = book('name1', '100', 'C', 'C++')
#print ('name1:', name1)
#
#name2 = book('name1', '100', 'C++', 'Python')
#
#print ('name2:', name2)
