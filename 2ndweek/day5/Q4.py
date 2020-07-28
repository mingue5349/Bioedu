#!/usr/bin/env python
d_persons = {'Guillaume':'Canada', 'Niklas':'Germany', 'Mark':'USA', 'Alex':'Swiss', 'Alberto':'Italia'}

class Person:
    def __init__(self, person):
        self.person = person
    def printnation(self):
        result = d_persons[self.person]
        return result

a = Person('Guillaume')
b = Person('Niklas')

print (a.printnation())
print (b.printnation())
