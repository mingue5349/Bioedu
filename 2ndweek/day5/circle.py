class Circle():
    def __init__(self,radius):
        self.radius = radius

    def R(self, radius):
        self.radius = radius
        print (self.radius)

    def area(self):
        result = (self.radius ** 2) * 3.14
        print (result)

    def around(self):
        result = (self.radius * 2) *3.14
        print (result)

circle = Circle(9)

circle.area()