class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


    def display(self):
        print(f"Area is {self.area()} and perimeter is {self.perimeter()}")

r = Rectangle(5, 10)
r.display()