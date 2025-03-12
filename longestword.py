#find the length of the longest word

def long(s):
    l = s.split()
    lun = 0
    for i in range(len(l)):
        if len(l[i]) > lun:
            lun = len(l[i])
        i +=1
    print(lun)


long("Theeeeee quick brown fox jumps over the lazy dog")