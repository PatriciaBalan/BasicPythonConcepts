#you are given a number N, you need to print its multiplication table.

def multiplicationTable(N):## in is a membership operator that is true if something is a member of sequence
    for i in range(1,11): ## i in range(x,y,z) means i goes from x to y-1 and increments z steps in each iteration
        print(i * N, end=" ") ## Separating by spaces using end =" "

#x = multiplicationTable(5)
# x = multiplicationTable(4)
x = multiplicationTable(10)
#x = multiplicationTable(7)