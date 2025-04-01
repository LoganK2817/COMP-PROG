import ROZLAND as roz
import artifact as ark

def main():
    ark.br()
    opp = input("D/E: ")

    if opp.lower() == "e":
        prePhrase = input("Enter for ROZLAND: ")
        print(roz.main(prePhrase))
    elif opp.lower() == "d":
        
        codedPhrase = input("Enter for DIRE: ")

        decodeKey = int(input("DecodeKey: "))

        buffer = ""

        buffer1 = ""

        for run in range(decodeKey):
            if run == 0:
                buffer = roz.main(codedPhrase)
            else:
                buf = roz.main(buffer)
                buffer = buf
                
        print(buffer)
    
    if input("RESET: ") == "True":
        ark.br()
        main()
    else:
        print("")
        
main()