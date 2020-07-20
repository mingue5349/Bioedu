#!/usr/bin/env python

chicken = 10

def countchicken(people):
    chicken = 20 #local variable
    chicken -= people
    print('{0} chicken remained.'.format(chicken))

def countchicken_global(people):
    global chicken #global variable
    chicken -= people
    print('{0} chicken remained.'.format(chicken))



print ('chicken:', chicken)
countchicken(5)
print('chicken:',chicken)
