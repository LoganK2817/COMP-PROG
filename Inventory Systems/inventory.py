import artifact as ark
import ast



"""
Currrent number of labeled ERRORS: 4
"""

class inventory:
    @staticmethod
    def refresh(file_id):
        with open(file_id, "r") as file:
            file_content = file.read().strip()
        totals = ast.literal_eval(file_content)
        
        return totals
    
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
    def save(file_id):
        with open(file_id, "w") as file:
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
    def write(write_action, item_id="null", count=0):
        if write_action =="new": # add new item to inventory
            print(inventory.new(item_id,count))
        elif write_action == "change":
            try:
                print(inventory.change(item_id,count))
            except:
                print("---ERROR 3; INVALID ITEM ID OR DEGREE; TRY AGAIN---")
        elif write_action == "remove":
            try:
                print(inventory.remove(item_id))
            except:
                print("---ERROR 4; INVALID ITEM ID; TRY AGAIN---")
            

class action:
    @staticmethod
    def read_all():
        user_commands.read("all")
        
    @staticmethod
    def read(item_id):
        user_commands.read("item",item_id)
        
    @staticmethod
    def save(file_id):
        inventory.save(file_id)
        
    @staticmethod
    def refresh(file_id):
        inventory.refresh(file_id)
    
    @staticmethod
    def write_new(local_inventory_id,item_id,count):
        local_inventory_id[item_id] = int(count)
