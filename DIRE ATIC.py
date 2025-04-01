import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import artifact as ark
import random





def main():
    
    encodedPhrase = input("Enter for DIRE: ")
    enPhLen = len(encodedPhrase)
    
    decodePhase = ""
    
    
    
    
    
    if enPhLen >= 4 and enPhLen <= 6:
        decodePhase = "p1"
    elif enPhLen >= 7 and enPhLen <= 9:
        decodePhase = "p2"
    elif enPhLen >= 10 and enPhLen <= 12:
        decodePhase = "p3"
    elif enPhLen >= 13 and enPhLen <= 15:
        decodePhase = "p4"
    elif enPhLen < 4:
        decodePhase  = "NULL"
    
    decodePhaseKey = {
        "p1" : 2,
        "p2" : 3,
        "p3" : 8,
        "p4" : 9
    }
    
    phaseShift = decodePhaseKey.get(decodePhase)
    slots = []
    point = 0
    
    index = 1
    run = 0
    for char in list(encodedPhrase):
        
        
        
        if index == 1: #-------------------------
            point += 1 # +1
            slots.append(point)
        elif index == 2: #-----------------------
            point += phaseShift + run # +K
            slots.append(point)
        elif index == 3: #-----------------------
            point += 1 # +1
            slots.append(point)
        elif index == 4: #-----------------------
            point -= phaseShift + run
            slots.append(point)
        
        run += 1
        index += 1
    
    print(slots)
    print(point)
    


main()