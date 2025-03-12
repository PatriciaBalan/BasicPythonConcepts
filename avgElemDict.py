#program that finds the avg value of all the elem in a list of dict

from collections import defaultdict

a = [{'a': 3, 'b': 8, 'c': 2}, {'a': 10, 'b': 2}, {'a': 7, 'b': 12, 'c': 8}]
dicts = [{"X": 5, "value": 200}, {"X": -2, "value": 100}, {"X": 3, "value": 400}]

def dict_mean(dict_list):
    mean_dict = {}
    for key in dict_list[0].keys():
        mean_dict[key] = sum(d[key] for d in dict_list) / len(dict_list)
    return mean_dict

print(dict_mean(a))


