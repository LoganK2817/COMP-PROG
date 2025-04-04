"""
This file is a dedicated function library, for reoccuring functions
to live so this file can just be imported as a library, and the 
functions called to save space and time.
-- LWK, 02/27/2025 6:43 PM MST
"""

import tkinter as tk
from tkinter import simpledialog



#-------------
def remove_dupes(preList):
    return list(dict.fromkeys(preList))

"""Takes a [list] and removes the duplicate
entries, then returns the new cleaned list."""

#--------------
# Function to get a non-numeric string input
def get_string(prompt):
    while True:
        try:
            value = simpledialog.askstring("Input", prompt)
            if value is None:  # Handle case where user cancels
                raise Exception("Input cancelled.")
            if value.isdigit():  # Ensure it's not purely numeric
                raise ValueError("Numbers are not allowed!")
            return value
        except ValueError as e:
            print("Error:", e)

"""Brings up a simpleDialog box for user
to imput a string, and returns the input."""

#--------------
# Function to get an integer input
def get_integer(prompt):
    while True:
        try:
            value = simpledialog.askstring("Input", prompt)
            if value is None:  # Handle case where user cancels
                raise Exception("Input cancelled.")
            return int(value)
        except ValueError:
            print("Error: Please enter a valid number.")

"""Brings up a simpleDialog box for user
to input a int, and returns the input."""

#--------------
# Line break function
def br(lines=12):
    print("-"*lines)
    
"""It prints a dash 12 times
unless otherwise specified, it ain't rocket science"""

#--------------
# program reset function

def reset(progMainFunc):
    
    resetVar = input("RESET? : ")    

    if resetVar == "1" or resetVar == "y" or resetVar == "yes":
        print("-"*6 +"RESETTING..." + "-"*6)
        progMainFunc()
    else:
        print("-"*6 +"SHUTTING DOWN..." + "-"*6)
        
"""The basic 'reset' function I use
in a lot of my programs, now all thats needed
is to call it and pass the 'main' func through"""

#--------------
