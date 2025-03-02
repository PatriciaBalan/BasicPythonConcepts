#You are given a string str, you need to print its characters at even indices(index starts at 0).

def characters(str):
    size = len(str)
    for i in range (0, size-1, 2):
        print(str[i], end="")

characters("DoctorPhenomenal")