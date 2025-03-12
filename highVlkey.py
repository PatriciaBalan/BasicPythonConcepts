#given a list of dictionaries, find the dict with highest value of a specific key

from collections import defaultdict

a = [{'a': 3, 'b': 8}, {'a': 10, 'b': 2, 'c': 5}, {'c': 12, 'a': 7}]

res = defaultdict(int)
for i in a:
    for k,v in i.items():
        res[k] = max(res[k], v)

print(dict(res))

