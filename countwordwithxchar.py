#given a list of words, count the no of words with more the 5 char

words = ["sun", "apple", "stradivarius", "nostradamus", "apollo", "lime"]

for i in range(len(words)):
    if len(words[i]) > 5:
        print(words[i])