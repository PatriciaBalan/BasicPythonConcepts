import numpy as np

#basic operations

l = [1,2,3,4,5]

arr = np.array(l, dtype=int)
print(arr)

arr1 = np.add(arr, 2)
print(arr1)

arr2 = arr - 1 #np.substract
print(arr2)

arr3 = arr *2 # np.multiply
print(arr3)

arr4 = arr / 2 #np.divide
print(arr4)

#np.power / arr**2
#--------------------------------------

#array of random numbers, calc mean, median, standard deviation

a = np.random.randint(100, size=(3, 5)) # check with and without size = 5; idem size 3,5
print(a) #int

b = np.random.rand(5) #floats
print(b)


c = np.random.choice([3,5,6,9], size =(3,5)) #similar cu int, check with 3,5 or without
print(c)

#--------------------------------------------

#create a numpy array and reshape it into a diff shape

n = np.array([[4,9,6,0], [5, 6, 7, 8]])
print(n.shape) # output 2,4 -> the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.


ar = np.array([1, 2, 3, 4], ndmin=5)
print(ar)
print('shape of array :', ar.shape)

#prod and sum of elem of an array
x = [1, 4, 6, 8, 19, 25, 46]
xx = np.array(x)
print(xx)

s = np.sum(xx)
print(s)

p = np.prod(xx)
print(p)
