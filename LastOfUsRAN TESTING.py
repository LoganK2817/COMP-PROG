import random
import math
import statistics

import tkinter as tk
from tkinter import simpledialog
root = tk.Tk() # Create a Tkinter root window
root.title("Movement Simulation") # Name the Tkinter window
root.geometry("400x250") # Size the Tkinter window

import plotting # The file where the point graphing takes palace
import artifact # My library for Commonly Used Modules

outFile = open("TLOF.txt", "w") # open/create outPut file
plotFile = open("TLOF_Points.txt", "w") # open/create plot output file


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
                
            print(f"{preCleaned}\n {postCleaned}")
                
            outFile.write(f"{zombie_typ} random walk of {stepVarNum} steps, {trials} trials:\n") #Writes the first line of output file for the given trail
            outFile.write(f"Mean = {round(avgDist, 2)} | CV = {round(cvDist, 2)}\n") #Writes the second line of output file for the given trail
            outFile.write(f"Max = {round(maxDist, 2)} | Min = {round(minDist, 2)}\n") #Wries thrid line of output file for the given trail
            outFile.write("-" * 40 + "\n") #Writes a visible line break under the block of trial information
    
    return True
    
# Create first label and entry field
label_1 = tk.Label(root, text="Enter How many steps to simulate:")
label_1.pack()
entry_1 = tk.Entry(root)
entry_1.pack()

# Create second label and entry field
label_2 = tk.Label(root, text="Enter How many trials to simulate:")
label_2.pack()
entry_2 = tk.Entry(root)
entry_2.pack()

# Create third label and entry field
label_3 = tk.Label(root, text="Enter what kind to simulate:")
label_3.pack()
entry_3 = tk.Entry(root)
entry_3.pack()


# Function to get input values
def get_inputs():
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

    # Debugging print to verify data types
    print(f"List Input (val1): {val1} (type: {type(val1)})")
    print(f"Integer Input (val2): {val2} (type: {type(val2)})")
    print(f"String Input (val3): {val3} (type: {type(val3)})")

    # Call simulate function with corrected values
    sim = simulate(val1, val2, val3)

    if sim == True:
        outFile.close() # closes the output file
        plotFile.close() # closes the plot file
        plotting.main()# call the plotting file to start making a scatter plot
        print("Plotting...")

button = tk.Button(root, text="Submit", command=get_inputs)
button.pack()

# Run the Tkinter event loop
root.mainloop()
