#check the status of an integer

def status(a, b, flag):
    if a > 0 or b < 0 and flag is False:
        return True
    elif a < 0 or b > 0 and flag is False:
            return True
    elif a < 0 and b < 0 and flag is True:
            return True
    else:
        return False

print(status(4,5, False))