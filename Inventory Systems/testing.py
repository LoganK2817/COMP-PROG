import inventory as inv

inventory_mem_file="test.txt"

local_inventory = {
    
}

print(local_inventory)
inv.action.write_new(local_inventory,"can",1)
print(local_inventory)