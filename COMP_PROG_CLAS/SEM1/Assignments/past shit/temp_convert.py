def fahrenheit_to_celsius(f):
    sum = f - 32
    C = 5 / 9 * sum
    return round(C,1)

def celsius_to_fahrenheit(c):
    F = (9 / 5) * c + 32
    return round(F,1)


def script():
    temp = float(input("Enter your temperature: "))
    convert_type = input("What temperature is the following already in? c/f : ")


    if convert_type.lower() == "f":
        print(f"Converted Temperature: {fahrenheit_to_celsius(temp)} ˚C")
    elif convert_type.lower() == "c":
        print(f"Converted Temperature: {celsius_to_fahrenheit(temp)} ˚F")
    else:
        print("invalid entry")

    restart = input("restart? y/n")
    if restart.lower() == "y":
        script()
    else:
        print("bye bye")


script()


