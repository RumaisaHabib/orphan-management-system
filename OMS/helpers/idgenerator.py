import random

def randomStr():
    l = [x for x in range(9)]
    l += [chr(x) for x in range(65, 65+26)]
    string = ""
    for x in range(32):
                string += str(l[random.randint(0, len(l) - 1)])

    return string

