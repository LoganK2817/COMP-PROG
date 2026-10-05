
class user_commands:
    
    @staticmethod
    def add():
        print("1")
        
    @staticmethod
    def minus():
        print("2")


input_options = {
    "add": user_commands.add,
    "minus": user_commands.minus
}

def main():
    
    command = input_options.get(input("enter command: "))
    
    print(f"Running: {command}")
    command()
    
    
    
main()