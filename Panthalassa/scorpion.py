import artifact as ark



def main():
    encoded = input("INPUT: ") # get input from user
    
    encoded_list = list(encoded) # convert user string to list of characters
    
    decodeKey = int(input("Decode: ")) # decode key from COVEY
    rozFactor = int(input("Roz Factor: ")) # roz factor from COVEY
    
    outputbuild = [] # where the output is built
    
    for item in encoded_list:  # this puts in a '-' for each character in the OG string
        outputbuild.append('-')    
    outputbuild[0] = encoded_list[0] # places the first character
    
    for num in range(decodeKey): # loops for every cycle 1 character AKA the decodekey
        indexPosition = num + 1 # makes the position it'll start looking at the encoded string at [1] to account for the first character constant
        outIndex = indexPosition*rozFactor # gets the position of the current character to be placed based on the current position in the encoded string * the rozKey, or cycle 1 step degree
        outputbuild[outIndex] = encoded_list[indexPosition] # take the character from the encoded string and places it in the correct spot in the decoded output
        
    
    remainders = encoded_list # makes a copy of the encoded list named 'remainders'
    for val in range(decodeKey+1): # this removes all the cycle 1 characters, +the first character, leaving the remainders list all cycle 2 characters
        remainders.pop(0)
    print(f"remainders: {remainders}")
    
    position = 0 # current position of the for loop in the output list 
    usedbank = 0 # current position of the for loop in the remainders list
    for item in outputbuild: # takes the remainders list and replaces the blank '-' spaces in the outputbuild with the cycle 2 characters in order
        if item == '-':
            outputbuild[position] = remainders[usedbank]
            usedbank +=1
        position += 1
    
    print(outputbuild)
    print(''.join(outputbuild))



main()