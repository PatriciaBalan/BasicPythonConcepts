class BankAccount():
    def __init__(self):
        self.balance = 0

    def deposit(self):
        amount = float(input("enter amount to be deposited"))
        self.balance += amount
        print("\n Amount deposited", amount)

    def withdraw(self):
        amount = float(input("enter the amount to be withdrawn"))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print("\n Net Available Balance=", self.balance)

s = BankAccount()

s.deposit()
s.withdraw()
s.display()