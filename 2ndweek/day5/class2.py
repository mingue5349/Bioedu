class Circle():
    pi = 3.14

    def area(self, radius):
        return self.pi*radius**2

circle = Circle()

pizza_area = circle.area(6)

print(pizza_area)