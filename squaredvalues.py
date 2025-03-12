#list of number -> create a new list with the squared values

def sq(l):
    #l = [2,4,5,3]
    x =[]
    for i in range(len(l)):
        x.append(l[i]**2)
        i +=1
    print(x)

(sq([2,4,5,3]))