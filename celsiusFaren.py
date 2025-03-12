#convert celsius to fahrenheit
#f = c * (9/5) +32

def transf(c):
    f = c * (9 / 5) + 32
    print(f)

transf(37.5)

def trans(f):
    c = (f-32) *  5/9
    print(round(c,3))
trans(99.5)
