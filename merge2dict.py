#given 2 dict -> merge them into one dict

d1 = {"apple": 1, "carrot": 2}
d2 = {"tomato": 3, "oil": 4, "apple":5}

d1.update(d2)
print(d1)

#remove a key-value pair

d1.pop("apple")
print(d1)