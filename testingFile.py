import tkinter as tk  

# Create the main application window
root = tk.Tk()
root.title("Tkinter Inputs Example")
root.geometry("400x250")  # Set window size

# Create labels and entry fields
label1 = tk.Label(root, text="Input 1:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Input 2:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Input 3:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

# Function to get input values
def get_inputs():
    val1 = entry1.get()
    val2 = entry2.get()
    val3 = entry3.get()
    print(f"Input 1: {val1}, Input 2: {val2}, Input 3: {val3}")

# Create a button to fetch input values
button = tk.Button(root, text="Submit", command=get_inputs)
button.pack()

# Run the Tkinter event loop
root.mainloop()
