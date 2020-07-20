#!/usr/bin/env python

d_persons = {'Guillaume' : 'Canada', 'Niklas' : 'Germany', 'Mark':'USA', 'Alex':'Swiss', 'Alberto':'Italia'}

#class 는 데이터와 함수를 동시에 갖고 있는 형태
class Person():
    nation = 'A nation'
    name = 'username'
    def setName(self, target):
        self.name = target
    def findNation(self, d_dict):
        self.nation = d_dict[self.name]
    def showName(self):
        print (self.name)
    def showNation(self):
        print (self.nation, end = '\n')


for i in range(len(d_persons)):
    PP = Person()
    PP.setName(list(d_persons.keys())[i])
    PP.findNation(d_persons)
    PP.showName()
    PP.showNation()

person1 = Person()        # person1 = 객체
person2 = Person()
person3 = Person()
person4 = Person()
person5 = Person()

    
