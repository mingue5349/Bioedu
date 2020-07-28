#!/usr/bin/env python

class Person:
    nation = 'A nation'

    def __init__(self, country):
        self.nation = country
    
    def showNation(self):
        print(self.nation)        

    def greeting(self):
        print('(method)greeting:', 'Hi')
    
    def hi1(self):
        self.greeting()           #method greeting
    def hi2(self):
        greeting()                #function greeting

def greeting():
    print('(function)greeting:', 'Hello!')
yune = Person()
yune.greeting()
print()
yune.hi1()
yune.hi2()

