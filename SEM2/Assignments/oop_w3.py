#An object is a entity that has properties and methods; a class is like a schematic for making objects

class Triangle:
    
    def __init__(self,length):
        self.length = length
      
#--------------  
        
tri1 = Triangle(4)
print(tri1.length)

#--------------



"""
The '__init__()' class method is used to initiate
the basic paramiters of a class right when it is called.
"""


"""
the self parameter is used to reference the working
instance of a class. it doesn't have to be 'self'
and can be renamed to whatever, so long as it's
the first parameter of any function in the class.
"""


#--------------


class Dog:
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age
        
    def bark(self):
        print(f"*chirp chirp* My name is {self.name}")
        
mia = Dog("Mia","Chihuahua/yorki","9 Weeks")
ellie = Dog("Ellie Mae","Chihuahua/yorki","9 Weeks")

mia.bark()
ellie.bark()

#--------------


class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.year = year
        self.model = model
        
    def start_engine(self):
        print(f"The Engine of the {self.make} {self.model} ({self.year}) is now running.")
        
        
toyota = Car("Toyota","Corolla",2012)

toyota.start_engine()