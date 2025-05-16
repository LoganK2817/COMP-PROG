def br():
    print("-"*12)



city_sightings = {"pigeon", "cat", "raccoon", "rat", "squirrel"}

mouintain_sightings = {"raccoon", "squirrel", "bobcat", "deer", "beaver"}

def cityOnly(): # list animals ONLY found in the city
    return city_sightings.difference(mouintain_sightings)

def bothAreas(): # list animals found in BOTH areas
    return city_sightings.intersection(mouintain_sightings)

def totalAnimals(): # list TOTAL animals across ALL areas
    return len(city_sightings) + len(mouintain_sightings)

def totalUni(area = "null"): # list TOTAL animals UNIQUE to EACH area
    just_city = len(city_sightings.difference(mouintain_sightings))
    just_mountain = len(mouintain_sightings.difference(city_sightings))
    
    if area == "null":
        return (just_city,just_mountain)
    elif area == "city":
        return just_city
    elif area == "mountain":
        return just_mountain
    
    

br()
print(f"Animals ONLY found in the CITY: {cityOnly()}")

br()

print(f"Animals found in BOTH areas: {bothAreas()}")

br()

print(f"TOTAL animals in BOTH areas: {totalAnimals()}")

br()

print(f"TOTAL UNIQUE animals in BOTH areas;\nCity: {totalUni('city')}\nMountain: {totalUni('mountain')}")
br()