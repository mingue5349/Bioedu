#!/usr/bin/env python

first = input('1st:')
second = input('2nd:')
third = input('3rd:')


#made a calculator
def calculator(num0, num1, op):
    if op == '+':
        result = int(num0) + int(num1)
    elif op == '-':
        result = int(num0) - int(num1)
    elif op == '/': 
        result = int(num0) / int(num1)
    elif op == '*':
        result = int(num0) * int(num1)
    else:
        result = "please input correct operator"
    return result

result = calculator(first, second, third)

print (result)
