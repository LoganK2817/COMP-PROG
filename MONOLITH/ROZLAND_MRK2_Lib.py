import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import IDKY.artifact as ark



def main(enteredPhrase = "N/A", PrintStatus = False):

    printStatus = PrintStatus

    
    startingPhrase = enteredPhrase

    endingPhrase = []

    picked_Slots = []
    current_slot = 0

    cypherIncrement = 3
    
    if printStatus:
        ark.br()
    
    for run in range(len(startingPhrase)*2):
        
        if current_slot in picked_Slots:
            if printStatus:
                print(f"Already Picked {current_slot}")
            current_slot += cypherIncrement
        elif current_slot > len(startingPhrase)-1:
            if len(endingPhrase) < len(startingPhrase):
                if printStatus:
                    print("out of range, shifting...")
                current_slot = 0
                cypherIncrement = 1
            else:
                if printStatus:
                    print("Out of range, lengths match, ending cycle...")
                break
        elif current_slot not in picked_Slots:
            if printStatus:
                print(f"adding index {current_slot}...")
            picked_Slots.append(current_slot)
            endingPhrase.append(startingPhrase[current_slot])
            current_slot += cypherIncrement
    if printStatus:    
        ark.br()       


    string = ''.join(endingPhrase)
    return string