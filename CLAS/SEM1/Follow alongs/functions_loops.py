def followAlong(num1,num2):
    var=num1 ** num2
    for i in range(4):
        var +=var
    return var


print(followAlong(2,2))
