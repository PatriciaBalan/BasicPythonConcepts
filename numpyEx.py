#implement a program that generates a numpy array with numbers from 0 -> 9
# and reshapes it into a 3x3 matrix

import numpy as np

a = np.arange(1, 10).reshape(3,3)
print(a)


#--------------------------------

#write a program that uses numpy to find the mean, median and standard deviation of a dataset.

b = np.arange(10)
bm = np.mean(b)
print(bm)

bme= np.std(b) #standard deviation
print(bme)

bv = np.var(b) #variance
print(bv)


#---------------------------------

#create a function that takes a list of numbers and returns the numpy array sorted in ASC

def srt(l):
    #l = [100,3, 25, 7, 75,88]
    q = sorted(np.array(l))
    print(q)
    w = np.array(l)
    print(np.sort(w))

srt([100,3, 25, 7, 75,88])

#----------------------------------
#given a list of lists create a 2d numpy array and find the sum of element in each row and column

l = [[1,2,3,4], [5,6,7,8]]
ar = np.array(l)
print(ar)
s = np.sum(ar)
s1 = np.sum(ar, axis = 0) #column
s2 = np.sum(ar, axis = 1) #row
print(s ,"total", s1 , "row", s2, "column")

#-----------------------------
#program that generates a random numpy array and find the max and min values

r = np.random.randint(10, size=(5))
mx = np.max(r)
mn = np.min(r)
print(r, mx, mn)

#-------------------------------------

#function that takes a numpy array and returns a new array with all elem squared

def squared():
    na = np.array([2,3,5])
    newar = np.square(na)
    print("initial array: ", na)
    print("new array: ", newar)

squared()


#------------------------------------

#given a numpy array, calculate the dot product of the array itself

n = np.array([1,2,3,4])
n2 = np.array([[1,2,3,4], [2,3,4,5]])
pr = np.prod(n)
pr2 = np.prod(n2)
print(pr, pr2)


#-----------------------------------
#create a program to calculate the inverse of a 2x2 matrix

A = np.array([[6, 1],
              [4, -2]])

print(np.linalg.inv(A))

#----------------------------------

#function that takes a numpy array and returns the transpose of the array

def trans():
    B = np.array([[2,3,4],[4,5,6]])
    nB = np.transpose(B)
    return nB

print(trans())


