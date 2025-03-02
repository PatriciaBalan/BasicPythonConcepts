list = [12,2,5,9,8,7]
list.sort(reverse=False)
print(list)

d1 = {1: 1, 2:4}
d2 = {3: 6, 4:16}

print({**d1, **d2})

x = 0.1
y = 0.2
z = x+y
print(z)
print(z == 0.3)

a = 10
b = 20
c = 30
print(pow(a, b, c)) # print(a**b%c)

A = 16
B = 15
print(A%B//A)


print(0.1 + 0.2 == 0.3) # false!!! nu se poate egal

a = [1, 2, 3]
a = tuple(a)

print(a) #error->tuple cannot be modify a[0]= 2

ls = [1, 2, 3, 4, 5]
nls = ls[1:4]
nls.append(6)
print(len(ls), len(nls))