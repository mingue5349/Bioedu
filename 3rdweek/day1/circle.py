#!/usr/bin/env python

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = self.radius**2 * math.pi
        return result


circle1 = Circle(3)

print(circle1.area())
