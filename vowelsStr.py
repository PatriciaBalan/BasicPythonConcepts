#create a list comprehension to extract vowels fom a given string

s = "randomevennumber"
v = ["a", "e", "i", "o", "u"]

news = [x for x in s if x in v]
print(news)