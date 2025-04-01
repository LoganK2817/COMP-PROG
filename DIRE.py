import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import artifact as ark
import random


#outFile = open("IDKY/EncodedText.txt", "w")



def main():
    
    encodedInput = list(input("Enter BS: "))
    decodeKey = int(input("Decode Key: "))
    ark.br()
    
    print(encodedInput)

    preBS = encodedInput

    slots = []

    postBS = []

    spot = 0
    syShift = 0
    
    buffer = ""
    
    for runs in range(decodeKey):
        while True:  
            if spot in slots:                       
                print(f"{spot} already picked") 
            else:
                if spot > len(preBS)-1:
                    print("Out of Range, shifting cypher")
                    syShift += 1
                    spot = 0
                else:
                    slots.append(spot)
                    postBS.append(preBS[spot])
                    print(f"added index {spot}")

            if syShift == 0:
                spot += 3
            elif syShift == 1:
                spot += 1
            elif syShift >= 2:
                break
            
            if len(slots) == len(preBS):       
                ark.br()
                print(preBS)
                print(postBS)
                try:
                    string = ''.join(postBS)
                    print(string)
                    #outFile.write(string)
                    #outFile.close()
                except TypeError:
                    print(TypeError)
                ark.br()
                buffer = string
            
            


ark.br()
main()

