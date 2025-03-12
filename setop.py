#given 2 sets -> union, intersection, diff

s1 = {2,3,5,"ana", "tomato"}
s2 = {3, 5, "tomato", 7}

u = list(s1.union(s2))
print(u)

i = list(s1.intersection(s2))
print(i)

d = list(s1.difference(s2))
print(d)