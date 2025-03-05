def find_average(list): 
    itemCount = 0;
    
    for item in list:
        itemCount += 1;   
        
        total = 0
        
    if itemCount > 1:  
        for num in list:
            total += num
            
        return round(total / itemCount,2)
    elif itemCount <= 1:
        return "None"
    
#----------------------#    
    
def reverse_words(StartString):
    words = StartString.split()
    reversedWords = []
    
    for word in words:
        reversedWords.append(word[::-1])
        
    return " ".join(reversedWords)
    


#----------------------#

greet = "Hello World"

print(greet[6])