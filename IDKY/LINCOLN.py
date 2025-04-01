import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import artifact as ark

import random


preSyph = "123456"




def scramble(inputVal):
    
    output = []
    buffer = []
    
    for char in inputVal:
        buffer.append(char)
 
        
    
    slots = []
    slot = 0
    for item in buffer:
        output.append(buffer[slot])
        
        nextSlot = random.randint(0,len(buffer)-1)
        
        if nextSlot in slots:
            print(f"Already Used {nextSlot}")
        elif nextSlot not in slots:
            print(nextSlot)
            slots.append(nextSlot)
            slot = nextSlot
    
    
    return buffer,output
        
        
print(preSyph)
print(scramble(preSyph))