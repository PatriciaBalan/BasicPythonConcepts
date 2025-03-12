#count how many times an elem appears in a list
from collections import Counter

#l = ["word", "sun", "apple", "stradivarius", "apple", "sun", "sun"]


def occu(l):

    x = Counter(l)
    print(x)

occu(["word", "sun", "apple", "stradivarius", "apple", "sun", "sun"])
