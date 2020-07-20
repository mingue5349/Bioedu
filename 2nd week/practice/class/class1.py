#!/usr/bin/env python

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
#    def setdata(self, first, second):
#        self.first = first
#        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

#a = FourCal()
#b = FourCal()

a = FourCal(4,2)
b = FourCal(5,6)


#a.setdata(4,2)
#b.setdata(5,6)

print (a.add())
print (b.mul())



#클래스의 상속


class  MoreFourCal(FourCal):
    
    def pow(self):
        result = self.first ** self.second
        return result

#메소드 오버라이딩
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = MoreFourCal(4,0)
b = MoreFourCal(5,0)
print(a.add())
print(a.div())
print(a.pow())

print (b.add())
print (b.div())
print (b.pow())










