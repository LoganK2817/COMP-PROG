import random
import math
import statistics
import sys
import os


import tkinter as tk
from tkinter import simpledialog
root = tk.Tk() # Create a hidden Tkinter root window
root.withdraw()  # Hide the main window


# Get the parent directory and add it to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import plotting # The file where the point graphing takes palace
import artifact # My library for Commonly Used Modules





outFile = open("TLOF.txt", "w") # open/create outPut file
plotFile = open("TLOF_Points.txt", "w") # open/create plot output file
plotName = "Unique End Points Simulated"



class ZombieTypes: # functions for the simulation of each zombie movement type
    @staticmethod
    def shambler():
        return random.choice(["east", "north", "west", "south"])
    
    @staticmethod
    def clicker():
        return random.choices(["east", "north", "west", "south"], weights=[1, 1, 1, 2])[0]
    
    @staticmethod
    def stalker():
        return random.choice(["east", "west"])
    
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
            
            filteredList = artifact.remove_dupes(endingPos)
            
            preCleaned = 0
            postCleaned = 0
            
            for pos in filteredList:
                plotFile.write(f"{pos}\n")
                postCleaned += 1
                
            for pos in endingPos:
                preCleaned += 1
                
            print(f"Total Points Collected: {preCleaned}\nUnique Points Collected: {postCleaned}")
                
            outFile.write(f"{zombie_typ} random walk of {stepVarNum} steps, {trials} trials:\n") #Writes the first line of output file for the given trail
            outFile.write(f"Mean = {round(avgDist, 2)} | CV = {round(cvDist, 2)}\n") #Writes the second line of output file for the given trail
            outFile.write(f"Max = {round(maxDist, 2)} | Min = {round(minDist, 2)}\n") #Wries thrid line of output file for the given trail
            outFile.write("-" * 40 + "\n") #Writes a visible line break under the block of trial information
  
def main(): # Main program calling and handling


    # Get inputs using the functions
    stepVariation = [artifact.get_integer("How Many Steps: ")]
    trials = artifact.get_integer("How Many Trials: ")
    typ = artifact.get_string("Zombie Kind? : ")

    # Destroy the Tkinter root window after input is collected
    root.destroy()

    print(f"{stepVariation} | {trials} | {typ}") # prints the inputed variables to the command line

    simulate(stepVariation, trials, typ.lower()) # passes the inputed variables through to the actual simulations
    
    outFile.close() # closes the output file
    plotFile.close() # closes the plot file
    plotting.main(plotName) # call the plotting file to start making a scatter plot
    
    

main() # calls the main function with the actual shit in it


# maybe next itteration will change the color of the dots on the graph for each trial. i.e; trial 1 is blue, trial 2 is red, ect.

