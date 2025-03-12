class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades


    def display(self):
        return self.name, self.age, self.grades

s = Student("John", 21, 9)
print(s.display())