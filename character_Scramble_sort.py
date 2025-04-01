
import artifact as ark
import random

preBS = ["a","b","c","d","e","f","A"]

slots = []

postBS = []

while True:
    
    
    ranSpot = random.randint(0,len(preBS)-1) # gives random number between 0 and the legnth of preBS -1, as indexing starts at zero

    if ranSpot in slots: # checks if the slot has already been picked
        print(f"{ranSpot} already picked")
    elif ranSpot not in slots: # if it has not been picked, at it to the list of picked ones and use it as the index number when checking against the srs list
        slots.append(ranSpot)
        postBS.append(preBS[ranSpot])
        print(f"added {ranSpot}")

    
    if len(slots) == len(preBS): # once the output scramble matches the length of the input scramble, end the loop and print before and after to double check accuracy
        ark.br()
        print(preBS)
        print(postBS)
        break
    


slots.sort()
postBS.sort()
ark.br()
print(slots)
print(postBS)

