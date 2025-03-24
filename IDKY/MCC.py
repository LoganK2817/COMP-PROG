import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import artifact as ark

import tkinter as tk


# 1 Gearbox = 4 small cogs + 1 andesite cassing 



class totals:
    gearBox = 0
    smallCogs = [4]
    andesiteCasing = 1


class Warehouse:
    
    
    @staticmethod
    def remove_item(item, amount):
        item_types = {
            "scog": ["smallCogs", "Small Cog"],
            "andcase": ["andesiteCasing", "Andesite Casing"],
            "gearbox": ["gearBox", "Gearbox"]
        }

        item_info = item_types.get(item)
        if not item_info:
            return 0  # Invalid item

        attr_name = item_info[0]
        item_count = getattr(totals, attr_name, [0])

        if item_count[0] >= amount:
            setattr(totals, attr_name, item_count - amount)
            return 1
        else:
            return 0
             
    @staticmethod
    def add_item(item, amount):
        item_types = {
            "scog": ["smallCogs", "Small Cog"],
            "andcase": ["andesiteCasing", "Andesite Casing"],
            "gearbox": ["gearBox", "Gearbox"]
        }

        print(f'Adding {amount} of {item}')
        

        item_info = item_types.get(item)
        if not item_info:
            return 0  # Invalid item

        attr_name = item_info[0]
        item_count = getattr(totals, attr_name, [0])

        if item_count[0] >= 1:
            setattr(totals, attr_name, item_count.append(amount))
            print("attribute changed...")
            return 1
        else:
            return 0
        
        
class Opperations:
    
    @staticmethod
    def crafter(item,ammount):
        return
            


def main():
    
    
    print(totals.andesiteCasing,totals.gearBox,totals.smallCogs)
    
    
    
    
    
    
    task = input("Enter Operation to perform (opp,item,count); ")
    
    
    task = task.split(",")
    
    itemID = task[1]
    
    itemCount = int(task[2])
    
    opp_types = {
        "add": Warehouse.add_item(itemID,itemCount),
        "remove": Warehouse.remove_item(itemID, itemCount),
        "craft": Opperations.crafter(itemID,itemCount)
    }
    

    print(totals.andesiteCasing,totals.gearBox,totals.smallCogs)
    
    reset()
    
    
def reset():
    
    try: restart = int(input("Restart Program? 1/0: "))
    
    except ValueError:
        print("ValueError")
        reset()
    
    if restart:
        print("resetting....")
        main()
    else:
        print("Stopping Program.... Good bye!")
    
    
main()