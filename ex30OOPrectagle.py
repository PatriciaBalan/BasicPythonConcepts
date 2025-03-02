#Design a Rectangle class with default attributes for length and width set to 1.
# Include methods to set these attributes and calculate the area.

class Rectangle:
    def __init__(self, width = 1, length = 1):
        self.width = width
        self.length = length

    def set_atrib(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width

rect = Rectangle()
print("Default area:", rect.area())

rect.set_atrib(4, 5)
print("Updated area:", rect.area())
