def remove_all_from_string(main_string, sub_string):
    start = 0
    result = main_string

    if sub_string == "":
        return main_string  # If the substring is empty, return the original string

    while True:
        index = result.find(sub_string, start)
        if index == -1:  # If not found, exit the loop
            break
        result = result[:index] + result[index + len(sub_string):]  # Slice and remove

    return result


def script():

    string_one = input("Enter First String: ")
    string_two = input("Enter Substring to Remove: ")

    print(remove_all_from_string(string_one, string_two))

    #asks the user if they would like to restart the program or not
    #and then does so if asked to.
    restart = str(input("Restart? y/n  "))
    if restart.lower() == "y":
        script()
    else:
        print("good byeeee")



script()