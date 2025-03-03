def br():
    print("-" * 30)


# Lists

exList = [1,2,3,4,5]

print(exList[2])

exList.append(6)
exList.remove(1)

for item in exList:
    print(item)
    
#-------------
br()
# Strings

exString = "Howdy, there."

print(exString[0:5])
print(len(exString))

for char in exString:
    print(char)

exSplit = exString.split(",")
print(exSplit)

newString = ",".join(exSplit)
print(newString)

#-------------
br()
# Functions

def greet(typ): # ---Parameter
    if typ == "how".lower():
        print("Howdy.")
    else:
        print("Sup.")
    
greet("how") # ---Argument


def add(a,b):
    return a+b

print(add(1,51))

#-------------
br()


def return_greatest(list):
    return "Greatest: " + str(max(list))


print(return_greatest([1,2,5,6,7,124,6236,3]))


def count_vowels(text):
    count = 0
    vowels = "aeiou"
    for char in text:
        if char.lower() in vowels:
            count += 1
    return "Vowel count: " + str(count)

print(count_vowels("Cheese pizza"))


def remove_value(lst, value):
    return [item for item in lst if item != value]


print(remove_value([1,2,3,4,5],5))


def reverse_string(s):
    return s[::-1]

print(reverse_string("Howdy, There"))