def counting(num):
    result = 0
    for i in range(num):
        result = result + i

    finresult = result + num
    return finresult


def script():

    user_num = int(input("Enter a number: "))


    choice = str(input("for, or while loop? f/w: "))


    if choice == "f":
        print(counting(user_num))
    elif choice == "w":
        result = 0
        i = 0
        while i < user_num:
            result += i
            i += 1

        finresult = result + user_num

        print(finresult)


    #asks the user if they would like to restart the program or not
    #and then does so if asked to.
    restart = str(input("Restart? y/n  "))
    if restart.lower() == "y":
        script()
    else:
        print("good byeeee")

script()