#remove vowels

def vowels(v):
    v.split()
    vo = ["a", "e", 'i', 'o', 'u']
    for i in range(len(v)):
        if v[i] not in vo:
            newv = v[i]
            print(newv, end='')
vowels("abracadrabra")



# count no of names starting with vowels

def v(x):
    l = x.split()
    vo = ("a", "e", 'i', 'o', 'u')
    ct = []
    for i in range(len(l)):
        if l[i].startswith(vo):
            ct.append(l[i])
    print(len(ct))

v("Ana are mere albastre")