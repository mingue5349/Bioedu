#!/usr/bin/env python

class Person: #클래스의 시작은 보통 대문자로 한다. 
    nation = 'A nation' #클래스 안의 변수 = 속성(nation).

    def greeting(self): #클래스 안의 함수 = method.
                        #해당 메소드는 Person 이라는 클래스의
                        #메소드 이다. 



yune = Person()
yune.greeting()
yune.printNation()
yune.changeNation('Korea')
