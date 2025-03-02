import random
import math
import statistics
import sys
import os

import tkinter as tk
from tkinter import simpledialog
root = tk.Tk() # Create a Tkinter root window
root.title("Movement Simulation") # Name the Tkinter window
root.geometry("400x250") # Size the Tkinter window
result = tk.Toplevel(width="400", height="400") # open a window for the simulation data
result.title("Simulation Data") # Name the Data window
result.withdraw() # hide the result window untill it's needed

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) # Get the parent directory and add it to the path
import plotting # The file where the point graphing takes palace
import artifact # My library for Commonly Used Modules

plotFile = open("TLOF_Points.txt", "w") # open/create plot output file

firstTime = False

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
    
def remake_Datawindow():
    result = tk.Toplevel(width="400", height="400") # open a window for the simulation data
    result.title("Simulation Data") # Name the Data window
    result.withdraw() # hide the result window untill it's needed

def simulate(stepVariation, trials, typ): # simulate the movement according to the variables passed through
    
    print("-*-*-*-*-Simulating...")
    
    zombie_types = { # word bank for the zombie type functions compaired to the abreviated entry variable
        "sham": ("Shambler", ZombieTypes.shambler),
        "click": ("Clicker", ZombieTypes.clicker),
        "stalk": ("Stalker", ZombieTypes.stalker),
    }

    if typ == "all": # deciphers the inputed zombie type according to the bank, and handles using them all. 
        walker_types = zombie_types.items()
    else:
        walker_types = [(typ, zombie_types.get(typ))]

    for walker_key, (zombie_typ, zombie_func) in walker_types: # runs the simulation for each zombie type selected
        for stepVarNum in stepVariation:
            endingDist = [] # stores the ending distance traveled at the end of each trial ran
            endingPos = [] # Stores the ending Position after each trial 
            for _ in range(trials): # simulates the movement for the desired amount of times according to the trial var passed
                x_pos, y_pos = 0, 0 # stores the location of the simulated zombie
                
                for _ in range(stepVarNum): # simulates the movment for the desired type for each step requested
                    direct = zombie_func()
                    if direct == "north":
                        y_pos += 1
                    elif direct == "south":
                        y_pos -= 1
                    elif direct == "east":
                        x_pos += 1
                    elif direct == "west":
                        x_pos -= 1

                dist_traveled = math.sqrt(x_pos**2 + y_pos**2) # calculates the distance traveled from origin with pythagorean theorem
                endingDist.append(round(dist_traveled, 2)) # adds the ending distance traveled to the endingDist list for later usage
                endingPos.append((x_pos,y_pos))
            
            avgDist = sum(endingDist) / len(endingDist) # finds average distance traveled out of the trials ran
            minDist = min(endingDist) # finds the min distance traveled out of the trials ran
            maxDist = max(endingDist) # finds the max distance traveled out of the trials ran
            stdDev = statistics.stdev(endingDist) if len(endingDist) > 1 else 0 #These two lines find
            cvDist = stdDev / avgDist if avgDist != 0 else 0 # The Coefficient of Variance of the trials 
            
            filteredList = artifact.remove_dupes(endingPos) # Filters the reoccuring points out of ending postion list
            
            preCleaned = 0 # count for how many points where collected - AKA how many trials
            postCleaned = 0 # count for how many unique points were found
            
            for pos in filteredList: # writes the unique positions 
                plotFile.write(f"{pos}\n")
                postCleaned += 1
                
            for pos in endingPos:
                preCleaned += 1
                
            print(f"End points Collected: {preCleaned}\nUnique Points: {postCleaned}")


            result.deiconify()

            outLine1=tk.Label(result, text=f"{zombie_typ} random walk of {stepVarNum} steps, {trials} trials:\n") # Writes the first line of the output window
            outLine2=tk.Label(result, text=f"Mean = {round(avgDist, 2)} | CV = {round(cvDist, 2)}\n") # Writes the second line of output window for the given trail
            outLine3=tk.Label(result, text=f"Max = {round(maxDist, 2)} | Min = {round(minDist, 2)}\n") # Wries thrid line of output window for the given trail
            outLine4=tk.Label(result, text="-" * 40 + "\n") # Writes a visible line break under the block of trial information
            outLine1.pack()
            outLine2.pack()
            outLine3.pack()
            outLine4.pack()
    
    return True
    
def get_inputs(): # Function to get input values
    global firstTime
    global plotFile
    
    print("-*-*-*-*-Passing Inputs...")
    
    sim = False
    
    # Convert first input into a list of integers
    val1 = entry_1.get().split(",")
    try:
        val1 = [int(item.strip()) for item in val1]  # Convert to integers
    except ValueError:
        print("Error: Input 1 must be a list of integers (e.g., 10, 20, 30)")
        return  # Stop execution if conversion fails

    # Convert second input into an integer safely
    try:
        val2 = int(entry_2.get())
    except ValueError:
        print("Error: Input 2 must be an integer!")
        return  # Stop execution if conversion fails

    # Third input remains a string
    val3 = entry_3.get()

    if not firstTime: # Check for if it's the first time running the program
        sim = simulate(val1, val2, val3)
        firstTime = 1
        if sim == True:
            plotFile.close() # closes the plot file
            print("-*-*-*-*-Plotting...")
            plotting.main()# call the plotting file to start making a scatter plot
    elif firstTime: # if it's not the first time, reopen the 'plotFile' and run simulation
        plotFile = open("TLOF_Points.txt", "w") # open/create plot output file
        plotting.closePlot()
        result.destroy()
        remake_Datawindow()

        sim = simulate(val1, val2, val3)
        if sim == True:
            plotFile.close() # closes the plot file
            print("-*-*-*-*-Plotting...")
            plotting.main()# call the plotting file to start making a scatter plot

def end_Program(): # Function to close the Tkinter window, thus ending the program.
    print("Terminating Program...")
    root.destroy()
    plotting.closePlot()



print("-*-*-*-*-Initialzing Program. opening window to collect variables...")


# Create first label and entry field -------------
label_1 = tk.Label(root, text="Enter How many steps to simulate:")
label_1.pack()
entry_1 = tk.Entry(root)
entry_1.pack()

# Create second label and entry field -------------
label_2 = tk.Label(root, text="Enter How many trials to simulate:")
label_2.pack()
entry_2 = tk.Entry(root)
entry_2.pack()

# Create third label and entry field -------------
label_3 = tk.Label(root, text="Enter what kind to simulate:")
label_3.pack()
entry_3 = tk.Entry(root)
entry_3.pack()


runButton = tk.Button(root, text="Submit", command=get_inputs) # Button for running the program with given values
runButton.pack() # set button alignment

Button = tk.Button(root, text="Close", command=end_Program) # Button for closing the window, thus ending the program
Button.pack() # set button alignment

root.mainloop() # Run the Tkinter event loop


"""
Next change terminal stage messages, to a window
that pops up with the stages instead?

Bring 'TLOF.txt' into a window instead of a file output?
"""