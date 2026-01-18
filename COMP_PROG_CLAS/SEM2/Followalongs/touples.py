def br():
    print("-"*32)



numbers = (1,2,3,4)

print(numbers[2])

br()

for num in numbers:
    print(num)
    
    
br()    
    
num1, num2, num3, num4 = numbers

print(num1)
print(num3)


br()

def get_position():
    x = 10
    y = 35
    
    return (x,y)

x,y = get_position()


print(type(get_position()))