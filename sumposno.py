#sum of positive numbers from a list

l = [1, 4, 6, -7, 0, -3]
s = 0
for i in l:
    if i > 0:
        s = s + i
    i = +1
print(s)
