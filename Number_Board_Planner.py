import IDKY.MCC.artifact as ark


inventory = {
    "a": 4,"b": 4, "c": 4, "d": 4, "e": 4
}






class inventory:
    totals = {
        "cans": 2
    }
    
    @staticmethod
    def new(item_id,count):
        inventory.totals[item_id] = count
        return f"Added {item_id} with a count of {count} to inventory"
    
    @staticmethod
    def add(item_id,count):
        current = inventory.totals.get(str(item_id))

def main():
    ark.br()
    print("Inventory management via python: V 0.0.1\nEnter Action: *read,write,close*\n")
    
    while True: #This is the loop of user input
        action = input("--*read,write,close*--\n")
        
        if action == "write":
            write_action = input("-add- OR -new- :\n")
            if write_action =="new":
                print(inventory.new(input("-New Item ID:\n"),input("-New Item Count:\n")))
        elif action == "close":
            break
        elif action == "read":
            read_action = input("-item- OR -all- :\n")
            if read_action == "all":
                print(inventory.totals)
            elif read_action == "item":
                print(inventory.totals.get(str(input("Entire Item ID: "))))
            
        else:
            print("invalid action")
        
    ark.br()
    
    
    
main()
ark.reset(main)