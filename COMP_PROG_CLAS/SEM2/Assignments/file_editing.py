

numFile = open("/Users/lwk/Documents/School/VSCODE/Projects/SEM 2/misc files/numbers.txt", "r")


numsColec = []

for item in numFile:
    print(item.strip())
    numsColec.append(int(item.strip()))

numFile.close()






largestNum = open("/Users/lwk/Documents/School/VSCODE/Projects/SEM 2/misc files/largest.txt", "w")

largestNum.write(str(max(numsColec)))