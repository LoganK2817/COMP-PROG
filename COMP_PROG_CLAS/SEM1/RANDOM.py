x = 5 


def thing():
    global x;
    x = x +5
    return x


print(x)
print(thing())