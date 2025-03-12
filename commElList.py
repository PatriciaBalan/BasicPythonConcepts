#create a program that finds the common elem between 2 lists and store into new one

l1 = ["apple", 1, 5, "cidru"]
l2 = ["soda", "apple", 1]

l = []

for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            l.append(l1[i])
print(l)