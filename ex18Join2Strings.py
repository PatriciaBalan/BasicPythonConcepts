# Function to join given strings

def combo_string(a, b):
    if (len(a) > len(b)):
        print("String a is longer then b")
        short = b
        longer = a
    elif (len(a) < len(b)):
        print ("string a is shorter then b")
        short = a
        longer = b

    return short + longer + short


print(combo_string("abscd", "abc"))