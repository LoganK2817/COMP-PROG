import ROZLAND as roz

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import artifact as ark


"""
Error Codes:
1 - input for decode to short
2 - input for decode to long
3 - invalid opperation
"""


def main():
    ark.br()
    
    
    

    prePhrase = input("Enter for ROZLAND: ")
    
    ark.br()
    
    print(f"Original: {prePhrase}\nEncoded: {roz.main(prePhrase)}")

    
    encodedPhrase = roz.main(prePhrase)
    
    
    
    decodeKey = 1
    
    if decodeKey == 1003:
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
        elif enPhLen > 15:
            decodePhase = "ERR 4"
        
        decodePhaseKey = {
            "p1" : 2,
            "p2" : 3,
            "p3" : 8,
            "p4" : 9
        }
        
        phaseShift = decodePhaseKey.get(decodePhase)
        
    else:
        decodePhase = "MANUEL"
        phaseShift = decodeKey
    

    

    buffer = ""

    timesRan = 0

    
    if decodePhase != "NULL" or decodePhase != "ERR 4":
        
        while True:
    
            for run in range(phaseShift):
                if run == 0:
                    buffer = roz.main(encodedPhrase)
                else:
                    buf = roz.main(buffer)
                    buffer = buf
            
            if buffer == prePhrase:
                ark.br()
                print(f"Finished with validated output")
                ark.br()
                print(f"Decode Key: {timesRan+decodeKey}")
                print(f"Character Count: {len(prePhrase)}")
                break
            if buffer != "123456789-123456789":
                timesRan += 1
                phaseShift += 1
            
        
    elif decodePhase == "NULL":
        print("Error code 1")
    elif decodePhase == "ERR 4":
        print("Error code 2")       

    
    reset()
    
    
def reset():
    if 1==1: #bool(input("RESET: "))
        ark.br()
        main()
    else:
        print("")
        
main()