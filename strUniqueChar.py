#implement a function that takes a list of strings
# and returns a set of unique chars present in all strings

str = ['abdra', 'cadrabra', 'watermelon', 'citron']

import string

def unique(str):
    c = set()
    for i in range(len(str)):
        ch = list(str[i])
        c.update(ch)
    print(sorted(c))

unique(['abdra', 'cadrabra', 'watermelon', 'citron'])


