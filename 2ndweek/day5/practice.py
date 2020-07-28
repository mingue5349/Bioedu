#!/usr/bin/env python

#기본적인 class 의 구조
class Coffee():             # 커피라는 클래스
    numCoffee = 10
    def Hello(self):            # Coffee 라는 클래스의 Hello 메소드
        print ('Hello')
        return 'Hi!'

group1_coffee = Coffee()    # Coffee 의 인스턴스(객체)
group2_coffee = Coffee()
group1_coffee.numCoffee     # 10

print (group1_coffee.numCoffee)
group1_coffee.Hello()











#1_coffee = [10,8,3]

#for i in range(1_coffee):
#    print ((i+1), '반', 1_coffee[i], '개 커피가 있어요')

