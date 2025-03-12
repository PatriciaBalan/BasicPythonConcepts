#write a function that uses a loop to calculate the factorial of a number
#Factorial of a non-negative integer, is multiplication of all
# smaller than or equal to n

num = 6
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i

print(f"factorial number of {num}  is {factorial}")


def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

num = 5
print("Factorial of", num, "is", factorial(num))
