

class Geometry:
    
    instances = 0 #track the # of instances of the class created
    
    def __init__(self,width,length):
        self.width = width
        self.length = length
        
        Geometry.instances += 1

print(Geometry.instances)


g1 = Geometry(16,25)
g2 = Geometry(18,24)
print(Geometry.instances)
g3 = Geometry(13,221)
g4 = Geometry(14,22)
print(Geometry.instances)