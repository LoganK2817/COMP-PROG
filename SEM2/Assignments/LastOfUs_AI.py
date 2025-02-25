import random
import math
import statistics
import sys  # Needed for command-line arguments

class ZombieTypes:
    @staticmethod
    def shambler():
        return random.choice(["east", "north", "west", "south"])

    @staticmethod
    def clicker():
        return random.choices(["east", "north", "west", "south"], weights=[1, 1, 1, 2])[0]

    @staticmethod
    def stalker():
        return random.choice(["east", "west"])

def simulate(walk_lengths, trials, typ):
    zombie_funcs = {
        "shambler": ZombieTypes.shambler,
        "clicker": ZombieTypes.clicker,
        "stalker": ZombieTypes.stalker
    }
    
    walker_types = ["shambler", "clicker", "stalker"] if typ == "all" else [typ]
    
    for walker in walker_types:
        zombie_func = zombie_funcs[walker]
        
        for steps in walk_lengths:
            distances = []
            
            for _ in range(trials):
                x, y = 0, 0  # Reset position for each trial
                
                for _ in range(steps):
                    direction = zombie_func()
                    if direction == "north":
                        y += 1
                    elif direction == "south":
                        y -= 1
                    elif direction == "east":
                        x += 1
                    elif direction == "west":
                        x -= 1
                
                dist = round(math.sqrt(x**2 + y**2), 1)
                distances.append(dist)
            
            avgDist = round(sum(distances) / len(distances), 1)
            minDist = round(min(distances), 1)
            maxDist = round(max(distances), 1)
            stdDev = round(statistics.stdev(distances), 1) if len(distances) > 1 else 0.0
            cvDist = round(stdDev / avgDist, 1) if avgDist != 0 else 0.0
            
            print(f"{walker.capitalize()} random walk of {steps} steps")
            print(f"Mean = {avgDist} | CV = {cvDist}")
            print(f"Max = {maxDist} | Min = {minDist}\n")

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 random_walk.py <steps_list> <trials> <walker_type>")
        return
    
    walk_lengths = list(map(int, sys.argv[1].split(",")))
    trials = int(sys.argv[2])
    typ = sys.argv[3]
    
    if typ not in ["shambler", "clicker", "stalker", "all"]:
        print("Error: Invalid walker type. Choose from 'shambler', 'clicker', 'stalker', or 'all'.")
        return
    
    simulate(walk_lengths, trials, typ)

if __name__ == "__main__":
    main()
