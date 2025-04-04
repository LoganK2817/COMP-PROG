import ROZLAND as roz
import artifact as ark


"""
Error Codes:
1 - input for decode to short
2 - input for decode to long
3 - invalid opperation
"""


def main():
    ark.br()
    opp = input("D/E: ")
    
    
    if opp.lower() == "e":
        prePhrase = input("Enter for ROZLAND: ")
        print(roz.main(prePhrase))
    elif opp.lower() == "d":
        
        encodedPhrase = input("Enter for DIRE: ")
        
        
        
        decodeKey = int(input("DecodeKey: "))
        
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

        buffer1 = ""

        
        if decodePhase != "NULL" or decodePhase != "ERR 4":
            
        
            for run in range(phaseShift):
                if run == 0:
                    buffer = roz.main(encodedPhrase)
                else:
                    buf = roz.main(buffer)
                    buffer = buf
                
            print(buffer)
        elif decodePhase == "NULL":
            print("Error code 1")
        elif decodePhase == "ERR 4":
            print("Error code 2")       
    else:
        print("Error code 3")
    
    reset()
    
    
def reset():
    if 1==1: #bool(input("RESET: "))
        ark.br()
        main()
    else:
        print("")
        
main()