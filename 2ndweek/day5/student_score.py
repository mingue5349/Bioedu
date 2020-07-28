class Score:
    def __init__(self, kor, eng, math):
        self.__kor = kor
        self.__eng = eng
        self.__math = math

    def showKorean(self):
        return self.__kor

    def showEnglish(self):
        return self.__eng

    def showMath(self):
        return self.__math

    def showEverage(self):
        result = self.__kor + self.__eng + self.__math
        return result/3

stuA = Score(100,90,80)

print (stuA.showEnglish())
print (stuA.showEverage())

