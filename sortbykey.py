#having a list of dictionaries sort based on a specific key


from operator import itemgetter

a = [{'a': 3, 'b': 8}, {'a': 10, 'b': 2, 'c': 5}, {'c': 12, 'a': 7}]

sorted_list = sorted(a, key=lambda x: x['a'])
print(sorted_list)


sorted_listt = sorted(a, key=itemgetter('a'))
print(sorted_listt)