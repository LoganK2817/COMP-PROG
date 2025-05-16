
# For loop summation code
def counting(num):
    result = 0
    for i in range(num+1):
        result = result + i
    return result

# While loop summation code
def w_loop(num):
    result = 0
    i = 0
    while i < num+1:
        result += i
        i += 1
    print(result)

def script():
    # user input for number and loop type
    user_num = int(input("Enter A Number: "))
    choice = str(input("What kind? f/w: "))
    
    
    if choice.lower() == "f":
        print(counting(user_num)) # calls For loop func
    elif choice.lower() == "w": 
        print(w_loop(user_num))

        
script()

# restarts the program
restart = str(input("Restart? y/n: "))
if restart.lower() == "y":
    script()
else:
    print("byeee")

