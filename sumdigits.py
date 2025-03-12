#sum of digits of a given no

def sum(x):
    s = 0
    while (x > 0):
        s += x % 10 # extract last digit
        x =  x // 10 #remove last digit
    print(s)
sum(12345)
