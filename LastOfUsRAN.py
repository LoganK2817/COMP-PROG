import random
import math
import statistics
import tkinter as tk
from tkinter import simpledialog
import plotting



# Create a hidden Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the main window

outFile = open("TLOF.txt", "w") #open/create outPut file
plotFile = open("TLOF_Points.txt", "w")

# Function to get an integer input
def get_integer(prompt):
    while True:
        try:
            value = simpledialog.askstring("Input", prompt)
            if value is None:  # Handle case where user cancels
                raise Exception("Input cancelled.")
            return int(value)
        except ValueError:
            print("Error: Please enter a valid number.")

# Function to get a non-numeric string input
def get_string(prompt):
    while True:
        try:
            value = simpledialog.askstring("Input", prompt)
            if value is None:  # Handle case where user cancels
                raise Exception("Input cancelled.")
            if value.isdigit():  # Ensure it's not purely numeric
                raise ValueError("Numbers are not allowed!")
            return value
        except ValueError as e:
            print("Error:", e)


def remove_dupes(preList):
    return list(dict.fromkeys(preList))



class ZombieTypes: # functions for the simulation of each zombie movement type
    @staticmethod
    def shambler(): #Simulate movement for shambler
        randt = random.randint(1,4)
        if randt == 1:
            return "east"
        elif randt == 2:
            return "north"
        elif randt == 3:
            return "west"
        elif randt == 4:
            return "south"
    @staticmethod
    def clicker(): #simulate movement for clicker
        randt = random.randint(1,5)
        if randt == 1:
            return "east"
        elif randt == 2:
            return "north"
        elif randt == 3:
            return "west"
        elif randt in [4,5]:
            return "south"
    @staticmethod
    def stalker(): #simulate movement for stalker
        randt = random.randint(1,2)
        if randt == 1:
            return "east"
        else:
            return "west"
    
def simulate(stepVariation, trials, typ): #simulate the movement according to the variables passed through
    
    
    zombie_types = { #word bank for the zombie type functions compaired to the abreviated entry variable
        "sham": ("Shambler", ZombieTypes.shambler),
        "click": ("Clicker", ZombieTypes.clicker),
        "stalk": ("Stalker", ZombieTypes.stalker),
    }

    if typ == "all": #deciphers the inputed zombie type according to the bank, and handles using them all. 
        walker_types = zombie_types.items()
    else:
        walker_types = [(typ, zombie_types.get(typ))]

    for walker_key, (zombie_typ, zombie_func) in walker_types: #
        for stepVarNum in stepVariation:
            endingDist = [] #stores the ending distance traveled at the end of each trial ran
            endingPos = []
            for _ in range(trials): #simulates the movement for the desired amount of times according to the trial var passed
                x_pos, y_pos = 0, 0 #stores the location of the simulated zombie
                
                for _ in range(stepVarNum): #simulates the movment for the desired type for each step requested
                    direct = zombie_func()
                    if direct == "north":
                        y_pos += 1
                    elif direct == "south":
                        y_pos -= 1
                    elif direct == "east":
                        x_pos += 1
                    elif direct == "west":
                        x_pos -= 1

                dist_traveled = math.sqrt(x_pos**2 + y_pos**2) #calculates the distance traveled from origin with pythagorean theorem
                endingDist.append(round(dist_traveled, 2)) #adds the ending distance traveled to the endingDist list for later usage
                endingPos.append((x_pos,y_pos))
            
            avgDist = sum(endingDist) / len(endingDist) #finds average distance traveled out of the trials ran
            minDist = min(endingDist) #finds the min distance traveled out of the trials ran
            maxDist = max(endingDist) #finds the max distance traveled out of the trials ran
            stdDev = statistics.stdev(endingDist) if len(endingDist) > 1 else 0 #These two lines find
            cvDist = stdDev / avgDist if avgDist != 0 else 0 #the CV of the trials 
            
            plotFile.write("Ending Posistions:\n") #Writes the first line of output file for the given trail
            
            filteredList = remove_dupes(endingPos)
            
            preCleaned = 0
            postCleaned = 0
            
            for pos in filteredList:
                plotFile.write(f"{pos}\n")
                postCleaned += 1
                
            for pos in endingPos:
                preCleaned += 1
                
            print(f"{preCleaned}\n {postCleaned}")
                
            outFile.write(f"{zombie_typ} random walk of {stepVarNum} steps, {trials} trials:\n") #Writes the first line of output file for the given trail
            outFile.write(f"Mean = {round(avgDist, 2)} | CV = {round(cvDist, 2)}\n") #Writes the second line of output file for the given trail
            outFile.write(f"Max = {round(maxDist, 2)} | Min = {round(minDist, 2)}\n") #Wries thrid line of output file for the given trail
            outFile.write("-" * 40 + "\n") #Writes a visible line break under the block of trial information
  
def main(): #Main program calling and handling


    # Get inputs using the functions
    stepVariation = [get_integer("How Many Steps: ")]
    trials = get_integer("How Many Trials: ")
    typ = get_string("Zombie Kind? : ")

    # Destroy the Tkinter root window after input is collected
    root.destroy()

    print(f"{stepVariation} | {trials} | {typ}") #prints the inputed variables to the command line

    simulate(stepVariation, trials, typ) #passes the inputed variables through to the actual simulations
    
    outFile.close() #closes the output file
    plotFile.close() #closes the plot file
    plotting.main() #call the plotting file to start making a scatter plot
    
    

main() #calls the main function with the actual shit in it


#maybe next itteration will change the color of the dots on the graph for each trial. i.e; trial 1 is blue, trial 2 is red, ect.
# check the ending Pos for reaccuring data, and discard or otherwise mark if so.
