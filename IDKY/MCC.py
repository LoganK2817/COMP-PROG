import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import artifact as ark

import tkinter as tk


# 1 Gearbox = 4 small cogs + 1 andesite cassing 



class totals:
    gearBox = 0
    smallCogs = 4
    andesiteCasing = 1


class Warehouse:
    
    @staticmethod
    def get_inventory():
        ark.br()
        print(f"Andisite Casings: {totals.andesiteCasing}\nGearBoxes: {totals.gearBox}\nSmall Cogs: {totals.smallCogs}")
        ark.br()
    
    
    @staticmethod
    def remove_item(item, amount):
        item_types = {
            "scog": ["smallCogs", "Small Cog"],
            "andcase": ["andesiteCasing", "Andesite Casing"],
            "gearbox": ["gearBox", "Gearbox"]
        }
        
        itemID = item
        itemInfo = item_types.get(item)
        
        ItemName = itemInfo[1]
        itemTitle = itemInfo[0]
        
        currentAmount = getattr(totals, itemTitle)
        
        
        if amount <= currentAmount:
            setattr(totals, itemTitle, currentAmount - amount)
        else:
            ark.br()
            print("ERROR Cannot Remove, not enough material.")
            ark.br()
            return 0
            
        

        
             
    @staticmethod
    def add_item(item, amount):
        item_types = {
            "scog": ["smallCogs", "Small Cog"],
            "andcase": ["andesiteCasing", "Andesite Casing"],
            "gearbox": ["gearBox", "Gearbox"]
        }
        itemID = item
        itemInfo = item_types.get(item)
        
        ItemName = itemInfo[1]
        itemTitle = itemInfo[0]
        
        currentAmount = getattr(totals, itemTitle)
        
        
        setattr(totals, itemTitle, currentAmount + amount)
        
        
class Opperations:
    
    @staticmethod
    def crafter(item,ammount):
        return
            


def main():
    
    Warehouse.get_inventory()
    
    
    task = input("Enter Operation to perform (opp,item,count); ")
    
    
    task = task.split(",")
    
    
    itemID = task[1]
    
    itemCount = int(task[2])
    
    oppType = str(task[0])
    
    if oppType.lower() == "add":
        Warehouse.add_item(itemID,itemCount)
    elif oppType.lower() == "remove":
        if Warehouse.remove_item(itemID,itemCount) == 0:
            print("Warehouse ERROR - Please try again.")
    elif oppType.lower() == "craft":
        Opperations.crafter(itemID,itemCount)
    else:
        print(f"Handling Error: Invalid Opperation: {oppType}")

    Warehouse.get_inventory()
    
    reset()
    
    
def reset():
    
    try: restart = int(input("Perform Another Action? 1/0: "))
    
    except ValueError:
        print("ValueError")
        reset()
    
    if restart == 1:
        print("resetting....")
        main()
    else:
        print("Stopping Program.... Good bye!")
    
    
main()