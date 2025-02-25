def greet(name):
    return f"Hello, {name}"

def add(num1,num2):
    sum = int(num1) + int(num2) 
    return sum

def is_even(number):
    return number % 2 == 0


def calculate_product(num1, num2):
    sum = add(num1, num2)
    product = sum * 2
    return product



def script():
    print(greet(input("Enter Your Name: ")))
    print(add(input("Enter a number: "), input("Enter another number: ")))
    print(is_even(int(input("Enter a number: "))))
    num1 = int(input("Enter num 1: "))
    num2 = int(input("enter num 2: "))
    print(calculate_product(num1, num2))

script()