import pygame
students = ["Mark","Ben","Jake"]

#make a lists of all simple data types
barg = ["Mark",[1,3,5],5.0]

#append a list
barg.append("Sam")

#getting a value using indexing
print(barg[1][2])

#make a lists of numbers
nums_list = [[1,3,5],[9,8,7]]

#editing a cell using indexing
nums_list[0][1] = 2

#loop over and print list
for index in range(len(nums_list)):
    print(nums_list[index],barg[index]) 

print("------------")

#loop through and sum up
for lists in nums_list:
    for num in lists:
        print(num)