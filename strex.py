# list of words -> concat them separated by space
from operator import truediv

words = ["apple", "banana", "yogurt", "carrot"]
print(" ".join(words))



# reverse a given string
def rev(s):
        l = s.split()
        l.reverse()
        return ' '.join(l)

print(rev("abc is"))



# sentence as input -> count the words

print("write your sentence ")
x = input()
print("sentence is ", x)
c = x.split()
print(len(c))


