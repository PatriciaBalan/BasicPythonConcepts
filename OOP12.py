import math

class Shape():

    def perimeter(self):
        pass
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

    def calculate_perimeter(self):
        return 4 * self.side

c = Circle(7)
c.calculate_area()
c.calculate_perimeter()
print("Area and perimeter for circle with radius = 7 is : ", c.calculate_area(), c.calculate_perimeter())

s = Square(15)
s.calculate_area()
s.calculate_perimeter()
print("Area and perimeter for square with side = 15 is : ", s.calculate_area(), s.calculate_perimeter())
