#2 list -> return their union(unique elem from both list

l1 = [1,2,5,8,9]
l2 = [1,9,7,5,3]

def uni(l1, l2):
    l = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] != l2[j]:
                l.append(l1[i])
            if l2[i] != l1[i]:
                l.append(l2[i])
    print(set(l))

uni([1,2,5,8,9], [1,9,7,5,3])