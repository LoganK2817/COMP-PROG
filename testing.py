import artifact as ark


startingPhrase = "Loganwadekunz2817"


endingPhrase = []

picked_Slots = []
current_slot = 0

cypherIncrement = 3
ark.br()
for run in range(len(startingPhrase)*2):
    
    if current_slot in picked_Slots:
        print(f"Already Picked {current_slot}")
        current_slot += cypherIncrement
    elif current_slot > len(startingPhrase)-1:
        if len(endingPhrase) < len(startingPhrase):
            print("out of range, shifting...")
            current_slot = 0
            cypherIncrement = 1
        else:
            print("Out of range, lengths match, ending cycle...")
            break
    elif current_slot not in picked_Slots:
        print(f"adding index {current_slot}...")
        picked_Slots.append(current_slot)
        endingPhrase.append(startingPhrase[current_slot])
        current_slot += cypherIncrement
        
ark.br()       


string = ''.join(endingPhrase)
print(string)