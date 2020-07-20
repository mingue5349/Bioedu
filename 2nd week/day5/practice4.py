#!/usr/bin/env python

class Person():
    s_str1 = 'str1'
    s_str2 = 'str2'
    def prtStr(self):
        out = self.s_str1 + self.s_str2
        print(out)
    def showS_str1(self):
        print(self.s_str1)


p1 = Person()
p1.showS_str1()
p1.prtStr()
