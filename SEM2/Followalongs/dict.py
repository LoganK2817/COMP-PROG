

def countUserWords():
    entered_words = {
        
    }
    
    while True:
        
        word = input("Enter Word: ")
        
        if word == "stop" or word == "Stop":
            break

        if word in entered_words: entered_words[word] += 1     
        elif word not in entered_words: entered_words[word] = 1
            
    for key, value in entered_words.items():
        print(f"{key} ---- {value}")
    


