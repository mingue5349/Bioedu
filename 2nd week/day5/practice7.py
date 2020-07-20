#!/usr/bin/env python

class Cat:
    def __init__(self):
        self.sleepy = True

    def snack(self):
        print('myeo~')

#클래스 상속 (class Cat 을 상속 받음). () 안에 부모클래스 이름 적음.
class KoShort(Cat):
#    def snack(self):      #부모 클래스와 공통되는 기능이므로 없어도 됨.
#        print('myeo~')
    
    def snack_Kor(self):
        print ('야옹')     # 자식 class에서 새롭게 추가된 메소드
    

minyong = KoShort()
minyong.snack()            # 상속되었으므로 결과값 나옴.
minyong.snack_Kor()


print(minyong.sleepy)
