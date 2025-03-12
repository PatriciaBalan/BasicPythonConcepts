#program that counts the number of occurrences of each character in a given string using a dict

from collections import Counter

s = "Mama are mere bune si tata are mere bune"
x = Counter(s)
print(x)


d= {e:s.count(e) for e in set(s)}
print(d)

