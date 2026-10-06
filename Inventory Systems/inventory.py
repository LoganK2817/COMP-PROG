import artifact as ark
import ast



"""
Currrent number of labeled ERRORS: 4
"""

class inventory:
    with open("inventory systems/inventory_testing.txt", "r") as file:
        file_content = file.read().strip()
    
    totals = ast.literal_eval(file_content)
    
    @staticmethod
    def new(item_id,count):
        inventory.totals[item_id] = int(count)
        return f"Added {item_id} with a count of {count} to inventory"
    
    @staticmethod
    def change(item_id,degree):
        current = inventory.totals.get(str(item_id))
        inventory.totals[item_id] = current + int(degree)
        return f"Changed {item_id} by {degree}; current is now {inventory.totals[item_id]}"
    
    @staticmethod
    def remove(item_id):
        inventory.totals.pop(item_id)
        return f"Removed {item_id}."
    
    @staticmethod
    def save():
        with open("inventory systems/inventory_testing.txt", "w") as file:
            file.write(str(inventory.totals))
        return "Saved :)"


class user_commands:
    
    @staticmethod
    def read(read_action,item_id="null"):
        if read_action == "all": # print full inventory
            print(inventory.totals)
        elif read_action == "item": # print single item count via id
            print(inventory.totals.get(str(item_id)))  
            
    @staticmethod
    def write():
        write_action = input("-change- OR -new- OR -remove-:\n")
        
        if write_action =="new": # add new item to inventory
            print(inventory.new(input("-New Item ID:\n"),input("-New Item Count:\n")))
        elif write_action == "change":
            try:
                print(inventory.change(input("-Item ID:\n"),input("-Change Degree:\n")))
            except:
                print("---ERROR 3; INVALID ITEM ID OR DEGREE; TRY AGAIN---")
        elif write_action == "remove":
            try:
                print(inventory.remove(input("-Item ID:\n")))
            except:
                print("---ERROR 4; INVALID ITEM ID; TRY AGAIN---")
            

class action:
    @staticmethod
    def read_all():
        user_commands.read("all")
        
    @staticmethod
    def read(item_id):
        user_commands.read("item",item_id)
        
        
    
