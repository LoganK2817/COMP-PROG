def br():
    print("--"*12)


dogs = {"German Shepherd", "Brittany", "Great Dane", "Chihuahua", "Maltese"} 
pets = {"RIR", "Maltese", "Brittany", "Parakeet"}

br()

for dog in dogs: # print all the dogs in the 'dogs' set
    print(dog)
    
br()
    
print(dogs.intersection(pets)) # print the dogs that are in both sets

br()

for dog in dogs.intersection(pets): # print the dogs that are in both sets
    print(dog)
    
br()

print(pets.difference(dogs)) # print the pets that aren't dogs

br()

for animal in pets.difference(dogs): # print the pets that aren't dogs
    print(animal)