#!/usr/bin/env python

class Cal:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        result = self.number1 + self.number2
        return result

    def sub(self):
        result = self.number1 - self.number2
        return result

    def div(self):
        result = self.number1 / self.number2
        return result

    def mul(self):
        result = self.number1 * self.number2
        return result

    def pow(self):
        result = self.number1 ** self.number2
        return result

    def defineEorO(self):
        if self.number1%2 == 0:
            result = "{} is even".format(self.number1)
            return result
        else:
            result = "{} is odd".format(self.nubmer1)
            return result
    
    def define3or7mul(self):
        if self.number1%3 == 0:
            if self.number1%7 ==0:
                result = "{} is mul of 3, 7.".format(self.number1)
            else:
                result = "{} is mul of 3.".format(self.number1)
        else:
            if self.number1%7 ==0:
                result = "{} is mul of 7.".format(self.number1)
            else:
                result = "{} is not mul of 3, 7.".format(self.number1)
        return result


num = Cal(2, 4)

print (num.defineEorO())
print (num.define3or7mul())
