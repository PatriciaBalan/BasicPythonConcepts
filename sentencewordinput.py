#program that takes a sentence and a word as input and check if the word is in

print("Enter your fraze ")
fraze = input()

print("enter the word ")
word = input()

f = fraze.split()
print(f)

for i in range(len(f)):
    if f[i] == word:
        print(True)
