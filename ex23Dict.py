# create a dictionary from a tuple list arr
def createD(arr):
    dict = {}

    arr = [("mark", 1), ("ilia", 2), ("c", 3)]

    for key, value in arr:
        dict[key] = value
    return dict
#---------------------------------------------


# insert into dictionary
def insert_dict(query, dict):
    dict[query[1]] = query[2]

# deleting from dictionary
def del_dict(query, dict):
    if query[1] in dict:
        del dict[query[1]]
        return True
    elif query[1] not in dict:
        return False

# print marks of required name
def print_dict(key, dict):
    if key in dict:
        print("Marks of " + key + " is " + dict[key])
        return True
    else:
        return False


def pair_sum(dict, arr, sum):
    sum = 8
    arr = [1, 2, 3, 3, 5]

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum:
                return True
    return False

#sorted dict
d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}

myKeys = list(d.keys())
myKeys.sort()

# Sorted Dictionary
sd = {i: d[i] for i in myKeys}
print(sd)

d = {2: 56, 1: 2, 5: 12, 4: 24}

print("Dictionary", d)

# Sorting and printing dictionary keys
for i in sorted(d.keys()):
    print(i, end=" ")

# accessing items from dictionary
    d = {"name": "Alice", 1: "Python", (1, 2): [1, 2, 4]}
    print(d["name"])
    print(d.get("name"))

#adding and update a dict
    d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    d["age"] = 22 # add
    d[1] = "python" #update

#---------------------------

    d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age': 22}
# Using del to remove an item - Removes an item by key.
    del d["age"]
    print(d)

# Using pop() to remove an item and return the value
    val = d.pop(1)
    print(val)

# Using popitem to removes and returns
# the last key-value pair.
    key, val = d.popitem()
    print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
    d.clear()
    print(d)

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")









