import artifact as ark

"""
Before--------------'Hello World'
After w/o hot-swap--'HlWlelo ord'
After w/ hot-swap---'slWlelo ord'
"""

def main():
    encoded = "Hlelo"
    
    encoded_list = list(encoded)
    
    decodeKey = 1
    
    outputbuild = []
    
    result = []
    
    for item in encoded_list:
        outputbuild.append(' ')    
    outputbuild[0] = encoded_list[0]
    
    for i in range(decodeKey):
        indexPosition = i + 1
        outputbuild[indexPosition*decodeKey] = encoded_list[indexPosition]
        
    
    remainders = encoded_list
    for val in range(decodeKey+1):
        remainders.pop(0)
    print(remainders)
    
    position = 0
    usedbank = 0
    for item in outputbuild:
        if item == ' ':
            outputbuild[position] = remainders[usedbank]
            usedbank +=1
        position += 1
    
    print(outputbuild)
    print(''.join(outputbuild))



main()

"""

hello_wolld 

"""
