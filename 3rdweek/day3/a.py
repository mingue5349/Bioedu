class C:
    def __init__(self):
        print("class C의 인스턴스가 생성됨")
        self.name = "ccc"
        self.age = 0

    def say_hi(self):
        print("hi")

    def add_age(self, n:int):
        self.age += n

    def __str__(self): # print() 로 호출되는 부분을
                       # 지정하는 메소드
        return "__str__호출됨"

    def __repr__(self):# 그냥 호출되는 부분을 지정하는 메소드
        return "__repr__호출됨"

    def __abs__(self): # abs(c)
        print("__abs__호출됨")

    def __len__(self): # len(c)
        print("__len__호출됨")

    def __add__(self, other): # 객체를 __add__ 메소드 안쓰고
                              # 그냥 '+' 로 더할 수 있음.
                              # 사칙연산 등 다양한 연관 메소드
                              # 존재함. 
        return self.age + other.age


