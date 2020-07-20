#!/usr/bin/env python

class Cat:
    def __init__(self):
        self.sleepy = True

    def snack(self):
        print('myeo~')

#클래스 상속 (class Cat 을 상속 받음). () 안에 부모클래스 이름 적음.
class KoShort(Cat, Dog):
    def snack(self):    
        print ('야옹')     # 메소드 오버라이딩. 자식 클래스에서 부모 클래스 메소드와 같은 메소드를 다시 지정 가능.    

minyong = KoShort()
minyong.snack()            # 오버라이딩되어 '야옹'이 출력됨.


print(minyong.sleepy)
