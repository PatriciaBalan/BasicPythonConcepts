
import string

s = "The quick brown fox jumps over the lazy dog."

# Check if each letter of the alphabet appears in `t`
for letter in string.ascii_lowercase:
    if s.lower().count(letter) == 0:
        print(False)
        break
else:
    print(True)