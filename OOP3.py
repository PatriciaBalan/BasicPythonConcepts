import math
from math import radians


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_circumference(self):
        return  2 * math.pi * self.radius


c = Circle(1.0)
print(c.calculate_area())
print(c.calculate_circumference())