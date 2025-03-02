def insert(s, element):
    s.add(element)
    return s
s={1,2,4}
print(insert(s, 5))


def remove_from_set(s, element):
    s.discard(element)

s={1,2,4,5}
print(remove_from_set(s, 1))


def sum_set(s):
    return sum(s)
s={1,2,4}
print(sum_set(s))


#add(): Adds an element to the set.
#clear(): Removes all elements from the set
#discard(): Removes an element from the set if present.
#remove(): Removes an element from the set. If the element is not present, it raises error.
#pop(): Removes and returns an arbitary set element. Raise error if the set is empty.
#union(): Returns the union of sets in a new set
#update(): Updates the set with the union of itself and others
#len(): Return the length of set.
#sorted(): Return a new sorted list from elements in the set.
#sum(): Return the sum of all elements in the set.


def common_in_set(a, b):
    return a & b

a = {"apple", "banana", 3}
b = {"apple", 3, 5}
print(common_in_set(a,b))


# Function to find difference in sets
# Should return the difference in sets
def diff(a, b):
    return a - b

a = {"apple", "banana", 3}
b = {"apple", 3, 5}
print(diff(a, b))


# Function to find union of sets
# Should return the union of sets
def all_in_set(a, b):
    return a | b

a = {"apple", "banana", 3}
b = {"apple", 3, 5}
print(all_in_set(a, b))


#Iterating over a set using enumerated for loop.
# Creating a set using string
test_set = set("geEks")

# Iterating using enumerated for loop
for id, val in enumerate(test_set):
    print(id, val)

#min or max

s1 = {4, 12, 10, 9, 4, 13}

print("Minimum element: ", min(s1))
print("Maximum element: ", max(s1))

#can be sorted but the print will be diff
sorted_s = sorted(s)

print("Minimum element: ", sorted_s[0])
print("Minimum element: ", sorted_s[-1])

