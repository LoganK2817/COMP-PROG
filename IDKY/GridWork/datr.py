import artifact as ark
import random as ran

ark.br()
print("DAY AT THE RACES!")



def main():
    
    class Horses:
        
        
        
        DownTownBrown = (0,20)
        MilkAndCreamy = (0,20)
        SeaBiscut = (0,20)
        Mommy = (0,20)
        
        @staticmethod
        def advance(horse):
            if horse == 1:
                front,back = Horses.DownTownBrown
                Horses.DownTownBrown = (front+1,back-1)
                if front == 19: return 1
            if horse == 2:
                front,back = Horses.MilkAndCreamy
                Horses.MilkAndCreamy = (front+1,back-1)
                if front == 19: return 2
            if horse == 3:
                front,back = Horses.SeaBiscut
                Horses.SeaBiscut = (front+1,back-1)
                if front == 19: return 3
            if horse == 4:
                front,back = Horses.Mommy
                Horses.Mommy = (front+1,back-1)
                if front == 19: return 4
            
            return 0
        
    
    class Display:
        
        @staticmethod
        def refresh():
            Display.frame(), Display.DownTownBrown(),Display.MilkAndCreamy(),Display.SeaBiscut(),Display.Mommy(),Display.frame()
        
        @staticmethod
        def frame():
            print("-*"*10+"|")
        @staticmethod
        def DownTownBrown():
            front, back = Horses.DownTownBrown
            print("-"*front+"X"+" "*back+"Down Town Brown")
        @staticmethod
        def MilkAndCreamy():
            front, back = Horses.MilkAndCreamy
            print("-"*front+"X"+" "*back+"Milk And Creamy")
        @staticmethod
        def SeaBiscut():
            front, back = Horses.SeaBiscut
            print("-"*front+"X"+" "*back+"Sea Biscut")
        @staticmethod
        def Mommy():
            front, back = Horses.Mommy
            print("-"*front+"X"+" "*back+"Mommy")

    print("--Wellcome to Day At The Races!--\n--Select a Horse To start--")
    playerBet = input("Place Your Bet (1,2,3,4): ")
    Display.refresh()     
    print("--Bet set, let the race begin!--")
   
    while True:
    
        if input(";press enter to advance;") != 0:
            horse = ran.randint(1,4)

            result = Horses.advance(horse)
            
            if result != 0:
                Display.refresh()
                
                if int(playerBet) == result:
                    print("Your Horse Won!!!")
                else:
                    print("Better luck next time!")
                
                break
            Display.refresh()

    
main()
