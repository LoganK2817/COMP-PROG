import artifact as ark



""" 
GPE = mass*gravity*height
KE  = 1/2(mass)(velocity)^2 | KE = Work
EPE = 1/2(k-spring const)(x-compression)^2
Work = Force * Distance

"""



class Formulas:
    class GPE:
        @staticmethod # regular Gravitational Potential Energy Formula
        def Solve_For_gpe(mass=0,gravity=0,height=0):
            if not mass: mass = float(input("Mass[Kg]: "))
            if not gravity: gravity = float(input("Gravity[m/s]: "))
            if not height: height = float(input("Height[m]: "))
            
            return mass*gravity*height
        
        @staticmethod # modified formula to solve for Mass (m) [Kg]
        def Solve_For_m(gravity=0,height=0,gpe=0):
            if not gpe: gpe = float(input("GPE[J]: "))
            if not gravity: gravity = float(input("Gravity[m/s]: "))
            if not height: height = float(input("Height[m]: "))
            
            return (gpe/gravity)/height
            
        @staticmethod # modified formula to solve for Gravity (g) [m/s]
        def Solve_For_g(mass=0,height=0,gpe=0):
            if not mass: mass = float(input("Mass[Kg]: "))
            if not height: height = float(input("Height[m]: "))
            if not gpe: gpe = float(input("GPE[J]: "))
            
            return (gpe/mass)/height
        
        @staticmethod # modified formula to solve for Height (h) [m]
        def Solve_For_h(mass=0,gravity=0,gpe=0):
            if not mass: mass = float(input("Mass[Kg]: "))
            if not gravity: gravity = float(input("Gravity[m/s]: "))
            if not gpe: gpe = float(input("GPE[J]: "))
            
            return (gpe/mass)/gravity
        
    class KE:
        @staticmethod # Regular Kenetic Energy Formula
        def Solve_For_ke(mass=0,velocity=0):
            if not mass: mass = float(input("Mass[Kg]: "))
            if not velocity: velocity = float(input("Velocity[m/s]: "))
            
            return 0.5(mass)*(velocity*velocity)
        
        
class Data_Handling:
    
    class First_Formula:
        a=1

def main():
    
    ark.br()
    """starting_Formula = input("Known/Starting formula: [gpe,ke,epe]")
    second_Formula = input("Unknown/Second formula: [gpe,ke,epe]")"""
    print(Formulas.GPE.Solve_For_m())

    ark.br()
    
    
    
if True:
    main()