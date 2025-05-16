def citation(Nametuple):
    first, middle, last = Nametuple
    return f"{last}, {first} {middle}".strip()



print(citation(("logan", "wade", "kunz")))