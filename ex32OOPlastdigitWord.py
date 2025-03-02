#Last Digit in Words:
# Write a class with a method that takes an integer and prints the last digit of that number in words.

class Digit:
    def last_digit(self, number):
        last_dgt = number % 10
        words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        return words[last_dgt]

niw = Digit()
print(niw.last_digit(12))
