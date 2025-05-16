student_info = ("Logan", 16, "Python") #make tuple

print(student_info)

student_info += ("VS Code",) #add fav editor to tuple
print(student_info)


student_info_list = [] #convert to list

for item in student_info:
    student_info_list.append(item)
    
student_info_list.append(2027) #add graduation year

student_info = tuple(student_info_list) # convert back to tuple

print(student_info)


name, age, favLang, favIDE, gradYear = student_info # unpack vars
    
    
print(name) #print individually
print(age)
print(favLang)
print(favIDE)
print(gradYear)    
     
for item in student_info: #print with loop
    print(item)
    
    
    
    
def getScores(): # func that returns tuple
    return (12,32,67)

print(getScores())