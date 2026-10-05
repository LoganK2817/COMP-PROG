import artifact as ark


"""
Currrent number of labeled ERRORS: 4
"""


class inventory:
    totals = {
        "cans": 2
    }
    
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


class user_commands:
    
    @staticmethod
    def read():
        read_action = input("-item- OR -all- :\n")
        if read_action == "all": # print full inventory
            print(inventory.totals)
        elif read_action == "item": # print single item count via id
            print(inventory.totals.get(str(input("Enter Item ID: "))))  
            
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
            
    

commands = {
    "read": user_commands.read,
    "write": user_commands.write
}



def main():
    ark.br()
    print("Inventory management via python: V 0.0.1\nEnter Action: *read,write,close*\n")
    
    while True: #This is the loop of user input
        action = input("--*read,write,close*--\n")
        action = action.lower()
        if action == "close":
            break
        else:
            #print(f"Running: {action}")
            command = commands.get(action)
            try:
                command()
            except:
                print("---ERROR 1; INVALID COMMAND; TRY AGAIN---")
        
        
    ark.br()
    
    
    
main()
ark.reset(main)