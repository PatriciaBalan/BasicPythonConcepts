class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display(self):
        return self.name, self.position, self.salary
    
def main():
    employees = []
    with open('employee.csv') as f:
        for line in f:
            employee = line.split('\t')
            name = employee[0]
            pos = employee[1]
            sal = employee[2]
            employees.append(Employee(name, pos, sal))

e = Employee("Marian", "economist", 2500)
print(e.display)






#given a csv file with employee data, create a class to represent an employee

import csv

# Open the CSV file for reading
with open('employees.csv', mode='r') as file:
    # Create a CSV reader with DictReader
    csv_reader = csv.DictReader(file)

    # Initialize an empty list to store the dictionaries
    data_list = []

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Append each row (as a dictionary) to the list
        data_list.append(row)

# Print the list of dictionaries
for data in data_list:
    print(data)