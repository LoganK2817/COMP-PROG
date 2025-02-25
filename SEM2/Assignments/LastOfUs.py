import random
import math
import statistics
import argparse

outFile = open("TLOF.txt", "w") #open/create outPut file

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
            
            avgDist = sum(endingDist) / len(endingDist) #finds average distance traveled out of the trials ran
            minDist = min(endingDist) #finds the min distance traveled out of the trials ran
            maxDist = max(endingDist) #finds the max distance traveled out of the trials ran
            stdDev = statistics.stdev(endingDist) if len(endingDist) > 1 else 0 #These two lines find
            cvDist = stdDev / avgDist if avgDist != 0 else 0 #the CV of the trials 
            
            outFile.write(f"{zombie_typ} random walk of {stepVarNum} steps, {trials} trials:\n") #Writes the first line of output file for the given trail
            outFile.write(f"Mean = {round(avgDist, 2)} | CV = {round(cvDist, 2)}\n") #Writes the second line of output file for the given trail
            outFile.write(f"Max = {round(maxDist, 2)} | Min = {round(minDist, 2)}\n") #Wries thrid line of output file for the given trail
            outFile.write("-" * 40 + "\n") #Writes a visible line break under the block of trial information
  
def main(): #Main program calling and handling

    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument("StepVar", type=str, help="Step Variations to process") #Assign the first entry when command line calling to 'StepVar'
    parser.add_argument("trialNum", type=int, help="Number of trials to run") #Assign the second entry when command line calling to 'trialNum'
    parser.add_argument("typ", type=str, help="Type of Zombie to simulate") #Assign the thrid entry when command line calling to 'typ'
    args = parser.parse_args() #Assign the calling of parse_args to 'args'

    
    try: #removes the comma from first entry and makes it into a int list
        stepVariation = [int(x) for x in args.StepVar.split(",")]
    except ValueError:
        print("Error: The first argument must be a comma-separated list of integers.")
        exit(1)


    
    print(f"{stepVariation} | {args.trialNum} | {args.typ}") #prints the inputed variables to the command line

    simulate(stepVariation, args.trialNum, args.typ) #passes the inputed variables through to the actual simulations
    
    outFile.close() #closes the output file

main() #calls the main function with the actual shit in it