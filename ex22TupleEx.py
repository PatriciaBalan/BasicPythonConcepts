# find a tuple size
#tuple -> ()

t = ("a", 1, "bob", "55")
tLen = len(t)
print(tLen)

#find the max and min k elemts

test_tuple =(5, 20, 3, 7, 6, 8) # initializing
print("Original tup is ", str(test_tuple))

k = 2 # initial. k
res =[]
test_tuple = list(sorted(test_tuple)) # transf into a list

for i, val in enumerate(test_tuple): # enumerate
    if i < k or i >= len(test_tuple) - k:
        res.append(val)
res = tuple(res)
print("extracted str is ", res)

# sum of tuple
def sum(tuple):
    test = list(tuple)
    count = 0
    for i in test:
        count +=i
    return count


test_tup = (5, 20, 3, 7, 6, 8)
print(sum(test_tup))


# tuple cube
a = [1, 2, 3, 4, 5]

# Creating list of tuples using list comprehension
res = [(n, n**3) for n in a]
print(res)

a = [1, 2, 3, 4, 5]

# Creating list of tuples using map and lambda
res = list(map(lambda n: (n, n**3), a))
print(res)