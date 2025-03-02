#You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.
#Note: str contains only lowercase English alphabets.


def cat_hats(str):
    rec = str.count("cat")
    rec1 = str.count("hat")
    print("Cat appears for " , rec, "hat appears for ", rec1)

def cat_hat(str1):
    if str1.count('cat')==str1.count('hat'):
        return True
    else:
        return False

print(cat_hat("cathat"))