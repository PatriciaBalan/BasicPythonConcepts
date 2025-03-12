#given a list of words, find the word with the maximum len and print it with his len

#li= ["word", "sun", "apple", "stradivarius"]

def word(li):
    max = 0
    wd = []
    for i in range(len(li)):
        if len(li[i]) > max:
            max = len(li[i])
            wd = li[i]
        i +=1
    print(max, wd)


word(["word", "sun", "apple", "stradivarius"])