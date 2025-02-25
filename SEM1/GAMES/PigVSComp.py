import random  
  
def player_turn():  
    round_score = 0  
    while True:  
        roll = random.randint(1, 6)  
        print(f"Player rolled a {roll}")  
          
        if roll == 1:  
            print("Rolled a 1! Round score reset to 0.")  
            round_score = 0  
            break  
        else:  
            round_score += roll  
            print(f"Player's round score: {round_score}")  
          
        choice = input("Type 'b' to bank your score or 'r' to roll again: ").strip().lower()  
          
        if choice == 'b':  
            print(f"Player banks {round_score} points.")  
            break  
        elif choice != 'r':  
            print("Invalid choice, round continues.")  
      
    return round_score  
  
def computer_turn():  
    round_score = 0  
    while round_score < 15:  
        roll = random.randint(1, 6)  
        print(f"Computer rolled a {roll}")  
          
        if roll == 1:  
            print("Computer rolled a 1! Round score reset to 0.")  
            round_score = 0  
            break  
        else:  
            round_score += roll  
            print(f"Computer's round score: {round_score}")  
      
    if round_score >= 15:  
        print(f"Computer banks {round_score} points.")  
      
    return round_score  
  
def play_game():  
    player_score = 0  
    computer_score = 0  
      
    while player_score < 100 and computer_score < 100:  
        print("\nPlayer's turn:")  
        player_score += player_turn()  
        print(f"Player's overall score: {player_score}")  
          
        if player_score >= 100:  
            print("Congratulations! Player wins!")  
            break  
          
        print("\nComputer's turn:")  
        computer_score += computer_turn()  
        print(f"Computer's overall score: {computer_score}")  
          
        if computer_score >= 100:  
            print("Computer wins! Better luck next time.")  
            break  
  
play_game()  
