import random
import math
import statistics
import argparse

outFile = open("TLOF.txt", "w")

class ZombieTypes:
    @staticmethod
    def shambler():
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
    def clicker():
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
    def stalker():
        randt = random.randint(1,2)
        if randt == 1:
            return "east"
        else:
            return "west"
    


def simulate(stepVariation, trials, typ):
    
    
    zombie_types = {
        "sham": ("Shambler", ZombieTypes.shambler),
        "click": ("Clicker", ZombieTypes.clicker),
        "stalk": ("Stalker", ZombieTypes.stalker),
    }

    if typ == "all":
        walker_types = zombie_types.items()
    else:
        walker_types = [(typ, zombie_types.get(typ))]

    for walker_key, (zombie_typ, zombie_func) in walker_types:
        for stepVarNum in stepVariation:
            endingDist = []
            
            for _ in range(trials):
                x_pos, y_pos = 0, 0
                
                for _ in range(stepVarNum):
                    direct = zombie_func()
                    if direct == "north":
                        y_pos += 1
                    elif direct == "south":
                        y_pos -= 1
                    elif direct == "east":
                        x_pos += 1
                    elif direct == "west":
                        x_pos -= 1

                dist_traveled = math.sqrt(x_pos**2 + y_pos**2)
                endingDist.append(round(dist_traveled, 2))
            
            avgDist = sum(endingDist) / len(endingDist)
            minDist = min(endingDist)
            maxDist = max(endingDist)
            stdDev = statistics.stdev(endingDist) if len(endingDist) > 1 else 0
            cvDist = stdDev / avgDist if avgDist != 0 else 0
            
            outFile.write(f"{zombie_typ} random walk of {stepVarNum} steps, {trials} trials:\n")
            outFile.write(f"Mean = {round(avgDist, 2)} | CV = {round(cvDist, 2)}\n")
            outFile.write(f"Max = {round(maxDist, 2)} | Min = {round(minDist, 2)}\n")
            outFile.write("-" * 40 + "\n")


        

    
    
    
def main():

    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument("StepVar", type=str, help="Step Variations to process")
    parser.add_argument("trialNum", type=int, help="Number of trials to run")
    parser.add_argument("typ", type=str, help="Type of Zombie to simulate")
    args = parser.parse_args()

    
    try:
        stepVariation = [int(x) for x in args.StepVar.split(",")]
    except ValueError:
        print("Error: The first argument must be a comma-separated list of integers.")
        exit(1)


    
    
    print(f"{stepVariation} | {args.trialNum} | {args.typ}")

    simulate(stepVariation, args.trialNum, args.typ)
    
    outFile.close()



main()