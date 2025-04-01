import random

preBS = [1,2,3,4,5,6,7,8,9,10]

slots = []

while True:
    
    
    choice = random.randint(1,len(preBS))

    if choice in slots:
        print(f"{choice} already picked")
    else:
        slots.append(choice)
        print("Nice Number")
        
    if len(slots) == len(preBS):
        print(preBS)
        print(slots)
        break
    
slots.sort()

print(slots)