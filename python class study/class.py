class Musician:
    title = 'Rockstar'      # class 변수

    def explanation(self):  # 메서드를 정의할 때 첫 인수는 항상 self로 지정해야 함.
        print('I am a {}!'.format(self.title))



drummer = Musician()
guitarlist = Musician()
drummer.explanation()

print (drummer.explanation())
print (drummer.title)
print (guitarlist.title)