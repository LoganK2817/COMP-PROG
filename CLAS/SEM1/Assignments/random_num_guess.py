import random


target = random.randint(1,100)



def script():
    print(target)
    while True:
        guess = int(input("Enter Your guess: "))

        if guess > target:
            print("Lower")
        elif guess < target:
            print("higher")
        elif guess == target:
            print("Correct!")
            break
    


script()


restart = input("restart? y/n")



if restart.lower == "y":
    script()
else:
    print("buh bye")