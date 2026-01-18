def br():
    print("------")

def bri():
    print("******")



def connection_board(num):
    tally = 0
    tally = tally + num
    
    
    br()
    print("bread")
    if tally >= 1:
        print("butter")
    else:
        bri()
    if tally >= 2:
        print("jelly")
    else:
        bri()
    if tally >= 3:
        print("sandwich")
    else:
        bri()
    if tally >= 4:
        print("lunch")
    else:
        bri()
    if tally >= 5:
        print("snack")
    else:
        bri()
    print("meal")
    br()





def script():

    guess = 1
    user_name = input("Enter Your Name Please: ")


    br()
    print("Welcome "+ user_name + " to the connections game!")
    br()
    print("You will be given two words, and you have to find the ones that connect them!")
    br()
    print("Good luck " + user_name + "!")


    connection_board(0)
    #----------
    while guess == 1:
        
        guess_1 = input("enter first guess: ")
        br()
        if guess_1.lower() == "butter":
            print("correct!")
            
            connection_board(1)
            guess += 1
            
        else:
            print("Try again!!")
    #----------
    while guess == 2:
        guess_2 = input("enter second guess: ")
        if guess_2.lower() == "jelly":
            print("correct!")
            
            connection_board(2)
            
            guess += 1
        else:
            print("Try Again!!")
    #----------
    while guess == 3:
        guess_3 = input("enter third guess: ")
        if guess_3.lower() == "sandwich":
            print("correct!")
            
            connection_board(3)
            
            guess += 1
        else:
            print("Try Again!!")
    #----------
    while guess == 4:
        guess_4 = input("enter fourth guess: ")
        if guess_4.lower() == "lunch":
            print("Correct!")
            
            connection_board(4)

            guess += 1
        else:
            print("Try Again!!")

    #----------
    while guess == 5:
        guess_5 = input("enter fith guess: ")
        if guess_5.lower() == "snack":
            print("Correct!")
            
            connection_board(5)

            guess += 1
        else:
            print("Try Again!!")

    #----------
    if guess == 6:
        print("You did it!!!!!!!!")
        bri()
        print("Congrats!")
        




    #asks the user if they would like to restart the program or not
    #and then does so if asked to.
    restart = str(input("Restart? y/n  "))
    if restart.lower() == "y":
        script()
    else:
        print("good byeeee")




script()



