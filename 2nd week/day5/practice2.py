#!/usr/bin/env python

class Person():
    nation = 'A nation'
    
    def greeting(self):
        print('greeting!')
    def printNation(self):
        print(self.nation)
    def changeNation(self, target):
        self.nation = target
        print('changeNation to {}'.format(target))


yune = Person()
yune.nation
yune.printNation
yune.printNation()
yune.changeNation('Korea')
yune.printNation()
