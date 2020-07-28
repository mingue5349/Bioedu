class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return(self.x,self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        return(self.x, self.y)

a =Point(4, 5)

print (a.get())
print(a.move(1,1))

a.setx(5)
a.sety(3)

print (a.get())
