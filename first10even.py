#print first 10 even numbers
def even():
    count = 0
    number = 0
    while count < 10:
        if number % 2 == 0:
            count += 1
            print(number, end=' ')
        number += 1
    print("first 10 even no are: " , number)
even()





