# Build a class Employee with multiple constructors
# that can initialize an employee object in different ways.


class Employee:
    def __init__(self, name, id = None, department = None):
        self.name = name
        self.id = id
        self.department = department

    def display(self):
        print(f"Name: {self.name}")
        if self.id:
            print(f"ID: {self.id}")
        if self.department:
            print(f"Department: {self.department}")


emp1 = Employee("John")
emp1.display()

emp2 = Employee("Elsa", 101)
emp2.display()

emp3= Employee("Tila", 102, "HR")
emp3.display()
