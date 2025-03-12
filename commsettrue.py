#given 2 sets -> check if there are some common elem

def st(s1, s2):
    s1 = list(s1)
    s2 = list(s2)
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                return True
        i +=1

print(st({1, 6, "ana"}, {6, "bob"}))