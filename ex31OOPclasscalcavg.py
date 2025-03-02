#Implement a Student class with attributes for name and a list of marks.
#Include a method to calculate the average and determine the grade.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.avg()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

student = Student("Alice", [92, 88, 91])
print(f"{student.name} Grade: {student.grade()}")