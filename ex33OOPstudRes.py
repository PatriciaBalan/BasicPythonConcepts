#Calculating Student Results: Develop a class to accept a student's name and marks in three subjects,
# then calculate and display the total and average marks.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def avg(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print(f"Name: {self.name}")
        print(f"marks : {self.total()}")
        print(f"avg : {self.avg()}")


sr = Student("Bob", [76, 84, 90])
sr.display()