#You'll be given a string str and x, you'll perform various operations on them.

#Your Task:
#This is a function problem.
#Do not take any input. just Complete the functions trim(), exists(), titleIt(), casesSwap().


def trim(str):
    return str.strip

def exists(str, x):
    return str.find(x)

def titleIt(str):
    return str.title()

def casesSwap(str):
    return str.swapcase()

def gfg(S):
    b = S.lower()
    if(b.startswith("gfg") and b.endswith("gfg")):
        print ("Yes")
    else:
        print ("No")


S = "gFgabcdEGfG"

str = "hello"
x = 3

print(str.strip())
print(str.title())
print(str.find(str, 1,3))
print(str.swapcase())

gfg(S)


