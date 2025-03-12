#function that takes a list of strings and returns the list sorted by len of the str

def srt(s):
    l = s.split()
    a = sorted(l, key=len)
    print(a)
    #sau sort
    l.sort(key=len)
    print(l)


srt("Theeeeee quick brown fox jumps over the lazy dog")