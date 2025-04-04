import ROZLAND_MRK2_Lib as ROZ
import ROZLAND as OLD_ROZ

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import artifact as ark


 
def main():
    
    ark.br()
    
    startingInput = input("Enter for ROZLAND KEY: ")
    
    ark.br()
    
    print(f"Original: {startingInput}")
    
    costiantDKupdates = False
    
    buffer = ""
    
    timesRan = 0
    
    while True:
        
        if timesRan == 0:
            firstCycle = ROZ.main(startingInput)
            print(f"Encode Degree 1 Phrase: {firstCycle}")
            ark.br()
            timesRan += 1
            buffer = firstCycle
        elif timesRan > 0:
            cycledPhrase = ROZ.main(buffer)
            timesRan += 1
            if cycledPhrase == startingInput:
                if costiantDKupdates:
                    print(f"Times ran: {timesRan-1}")
                ark.br()
                print("Finished will validated output")
                ark.br()
                print(f"Decode Key: {timesRan-1}")
                print(f"Character Count: {len(startingInput)}")
                ark.br()
                break
            elif cycledPhrase != startingInput:
                buffer = cycledPhrase
                if costiantDKupdates:
                    print(f"Times ran: {timesRan-1}")

    ark.reset(main)
    
    
main()
        
