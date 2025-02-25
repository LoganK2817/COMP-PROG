def get_highest(n1,n2):
    if n1 > n2:
        return n1
    elif n1 <n2:
        return n2
    else:
        return "neither"



print(get_highest(1,2))

print(get_highest(522,11))

print(get_highest(1,1))