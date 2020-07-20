#!/usr/bin/env python

class Cat():
    def __init__(self):    #부모클래스의 초기화 메소드 덕분에 자식 클래스의 초기화는 불필요
        self.sleepy = True
    def snack(self):
        print('myeo~')

class KoShort(Cat):
    def setAge(self, Age):
        self.__age = Age  #__로 시작하는 '비공개'속성은 클래스 밖에서 접근 불가
        print ("Set age to {0}.".format(Age))
    def showAge(self):
        print("{0} years old.".format(self.__age))
    def snack(self):
        print ('야옹')

minyong = KoShort()
minyong.setAge(7)
minyong.snack()
minyong.showAge()
print(minyong.__age)  #클래스 밖에서 개체의 비공개 속성에 접근할 수 없어 error 메세지 출력. 
