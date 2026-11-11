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


debug_text = True
cypher_text = False

def main():
    starting_string = input("INPUT: ")
    
    
    preString = list(starting_string)
    if debug_text: print(f"DEBUG TEXT:: PreString: {preString}")
    charCount = len(preString)
    if debug_text: print(f"DEBUG TEXT:: CharCount: {charCount}")
    firstChar = preString[0]
    if debug_text: print(f"DEBUG TEXT:: FirstChar: {firstChar}")
    
    checkedIndexs = []
    currentIndex = 0
    endString = []
    cypherShift = 0
    
    letterDigit = alphabet_to_digit.get(firstChar.lower())
    if debug_text: print(f"DEBUG TEXT:: LetterDigit= {letterDigit}")
    newletterDigit = letterDigit + charCount
    while newletterDigit > 26: 
        newletterDigit -= 26
    if debug_text: print(f"DEBUG TEXT:: New Letter= {newletterDigit}:{digit_to_alphabet.get(newletterDigit)}")
    shiftedLetter = digit_to_alphabet.get(newletterDigit)
    
    while True:
        
        
        
        if currentIndex in checkedIndexs:
            if cypher_text: print(f"index '{currentIndex}' already used, skipping")
        else:
            if currentIndex > charCount-1:
                if cypher_text: print("Current Index out of range, Shifter cyper to phase 2")
                cypherShift += 1
                currentIndex = 0
            else:
                checkedIndexs.append(currentIndex)
                endString.append(preString[currentIndex])
                
        if cypherShift == 0:
            currentIndex += 3
        elif cypherShift == 1:
            currentIndex += 1
        elif cypherShift >= 2:
            break
            
        if len(checkedIndexs) == charCount:
            result = []
            for char in endString:
                if char.lower() == firstChar.lower(): result.append(shiftedLetter)
                else: result.append(char)
            print(''.join(endString))
            print(''.join(result))
            break
    
ark.br(24)
main()
ark.br(24)