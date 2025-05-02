"""string = "Logan Wade Kunz|8/17/08|6'1"


name,dob,height = string.split("|")

print(string)
print(name)
print(dob)
print(height)"""

import sys


def extract(inString):
    name,dob,height = inString.split("_")

    return f"{name}, born {dob}, is {height}"
    


def main():
    inString = sys.argv[1]
    print(extract(inString))
    
if __name__ == "__main__":
    main()