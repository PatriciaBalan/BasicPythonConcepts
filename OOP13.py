class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        self.team_size = team_size
        super().__init__(name, salary)

    def display_details(self):
        return f"{super().display_details()}, Team Size: {self.team_size}"

class Engineer(Employee):
    def __init__(self, name, salary, programming_language):
        self.programming_language = programming_language
        super().__init__(name, salary)

    def display_details(self):
        return f"{super().display_details()}, Programming language: {self.programming_language}"

m = Manager("John", 10000, 10)
e = Engineer("bob", 5000, "python")
print(m.display_details())
print(e.display_details())