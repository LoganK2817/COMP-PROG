import artifact as ark


"""
I was inspired to create this program by the Engima Machine.
I've created a encryption program before, but learning about 
the Enigma made me see the flaws of my own system. 

So now i've sought out to correct these flaws and create 
a encyrtption program that cannnot be solved bassed on 
character substitution or guess work alone.

Wish me luck.
    -LWK, 11/09/2026 ; 7:20 PM

"""
##########
"""
Notes:

- user input for:
    * hot-swap shift degree, 
    * add the character count to hot-swap shift degree or not
    * ROZ degree
- organize varibles more
- class's ? 
"""
##########
alphabet_to_digit = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}

digit_to_alphabet = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i',
    10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q',
    18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
}

# debug variables to control printed output
debug_text = True
cypher_text = False

class ui:
    @staticmethod
    def getinputstring():
        return input("INPUT: ") # Get string from user
    
    @staticmethod
    def getrozfactor():
        return input("ROZ FACTOR: ")

class setup:
    # prework on input string
    preString = list(ui.getinputstring()) # convert it into a list for better manipulation
    if debug_text: print(f"DEBUG TEXT:: PreString: {preString}")
    
    charCount = len(preString) # get count of characters in string, used for the letter hot-swap and ending verification
    if debug_text: print(f"DEBUG TEXT:: CharCount: {charCount}")
    
    # first charcter work
    firstChar = preString[0] # get the first character in the string, this is the one that will be hot-swapped
    if firstChar == ' ': # if the first character is a empty space, move along until a english letter is found.
        index = 1
        while True:
            firstChar = preString[index]
            if not firstChar == ' ': break
            else: index += 1
    if debug_text: print(f"DEBUG TEXT:: FirstChar: {firstChar}")

    # letter hot-swap setup
    letterDigit = alphabet_to_digit.get(firstChar.lower()) # gets the number that corrisponds to the first character
    if debug_text: print(f"DEBUG TEXT:: LetterDigit: {letterDigit}")
    
    newletterDigit = letterDigit + charCount # uses the first letter digit and adds the character count to shift the letter
    while newletterDigit > 26: # if the ending int is > 26, take away 26 until it falls into range, aka wrap to the beginning of the alphabet
        newletterDigit -= 26
    if debug_text: print(f"DEBUG TEXT:: New Letter:  {newletterDigit}:{digit_to_alphabet.get(newletterDigit)}")
    
    shiftedLetter = digit_to_alphabet.get(newletterDigit) # convert this new digit number into an actual letter to be hot-swapped

def main():
    
    rozFactor = int(ui.getrozfactor())
    
    # basic cypher variables 
    checkedIndexs = [] # list of indexes that have been added to the output build already.
    currentIndex = 0 # variable to keep track of the current index location of the algorithm 
    endString = [] # the list where the output is built
    cypherShift = 0 # keeps track of what cycle the cypher is on
    decodeKey = 0
    shift = 0
    
    #cypher loop
    while True:
        
        if currentIndex in checkedIndexs:
            if cypher_text: print(f"index '{currentIndex}' already used, skipping")
        else:
            if currentIndex > setup.charCount-1:
                if cypher_text: print("Current Index out of range, Shifter cyper to phase 2")
                cypherShift += 1
                currentIndex = 0
            else:
                checkedIndexs.append(currentIndex)
                endString.append(setup.preString[currentIndex])
            
        # the cypherShift determines what cycle the algorithm is on        
        if cypherShift == 0: # cycle 1, primary run
            currentIndex += rozFactor
        elif cypherShift == 1: # cycle 2, clean-up run
            if shift == 0:
                decodeKey = len(endString)-1
                shift +=1
            currentIndex += 1 
        elif cypherShift >= 2: # cycle 3, hot-swap run
            result = []
            for char in endString:
                if char.lower() == setup.firstChar.lower(): result.append(setup.shiftedLetter)
                else: result.append(char)
            print(''.join(endString))
            print(''.join(result))
            print(f"Decode Key: {decodeKey}")
            break
            
    
ark.br(24)
main()
ark.br(24)