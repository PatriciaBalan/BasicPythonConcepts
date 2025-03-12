# check if a list is sorted ASC

def liso(l):
    if sorted(l) == l:
        return True
    else:
        return False

print(liso(["abdra", "cadra", "alba", "rada"]))

print(liso(["a", "b", "c", "d"]))