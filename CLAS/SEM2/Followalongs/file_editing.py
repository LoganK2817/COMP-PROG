import random

randNum = str(random.randint(1,6))

file_greets = open("/Users/lwk/Documents/School/VSCODE/Projects/SEM 2/Followalongs/greetings.txt", "r")

for line in file_greets:
    print(line.strip)


test_file = open("/Users/lwk/Documents/School/VSCODE/Projects/SEM 2/misc files/numbers.txt", "w")

test_file.write()




