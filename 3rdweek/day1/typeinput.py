#!/usr/bin/python3

letter = input("input a letter:")

if letter.isalpha() == True:
    print (letter + " is string")

if letter.isdigit() == True:
    print(letter + " is digit")
