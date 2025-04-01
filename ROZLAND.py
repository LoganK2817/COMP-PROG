import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import artifact as ark
import random





def main(phrase="N/A"):
    
    if phrase == "N/A":
        x = list(input("Enter BS: "))
        print(x)
        preBS = x
    elif phrase != "N/A":
        preBS = list(phrase)

    slots = []

    postBS = []

    spot = 0
    syShift = 0
    
    
    while True:
        
        
        
        if spot in slots:
            if phrase == "N/A":
                print(f"{spot} already picked") 
        else:                                           # if it has not been picked, at it to the list of picked ones and use it as the index number when checking against the srs list
            if spot > len(preBS)-1:
                if phrase == "N/A":
                    print("Out of Range, Shifting cypher")
                syShift += 1
                spot = 0
            else:
                slots.append(spot)
                postBS.append(preBS[spot])
                if phrase == "N/A":
                    print(f"added {spot} index")

        if syShift == 0:
            spot += 3
        elif syShift == 1:
            spot += 1
        elif syShift >= 2:
            break
        
        if len(slots) == len(preBS):
            
            if phrase == "N/A":      
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
            elif phrase != "N/A":
                string = ''.join(postBS)
                return string
            break
            
ark.br()

