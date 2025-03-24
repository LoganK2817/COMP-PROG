student_info = ("Logan", 16, "Python")

print(student_info)

student_info += ("VS Code",)
print(student_info)


student_info_list = []

for item in student_info:
    student_info_list.append(item)
    
student_info_list.append(2027)

student_info = tuple(student_info_list)

print(student_info)


name, age, favLang, favIDE, gradYear = student_info
    
    
print(name)
print(age)
print(favLang)
print(favIDE)
print(gradYear)    
    
for item in student_info:
    print(item)
    
    
    
    
def getScores():
    return (12,32,67)

print(getScores())