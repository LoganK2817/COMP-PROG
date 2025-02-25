import tkinter as tk
from tkinter import simpledialog


def do_research():
    Sustenance = int(simpledialog.askstring("Input", "Food Mass?"))
    adult_num = int(simpledialog.askstring("Input", "Adult Pair #"))
    baby_num = int(simpledialog.askstring("Input", "# of Babies"))
    month = 1
    meg_total = adult_num + baby_num

    # Prepare initial data for the first month
    month_one = [month, adult_num, baby_num, meg_total]

    # Open the CSV file for writing
    megalodons_file = open("/Users/lwk/Documents/School/VSCODE/Projects/SEM 2/misc files/megalodons.csv", "w")

    # Write the CSV headers and first month's data
    megalodons_file.write(f"Number of pairs that can be supported: {Sustenance}\n\n")
    megalodons_file.write("-Table of Megalodon Pairs-\n")
    megalodons_file.write("Month,Adults,Babies,Total\n")
    megalodons_file.write(f"{month},{adult_num},{baby_num},{meg_total}\n")

    # Simulate the population growth
    while meg_total <= Sustenance:
        month += 1
        temp_baby = baby_num
        baby_num = adult_num  # Babies are produced by adults
        adult_num += temp_baby  # Babies mature into adults
        meg_total = adult_num + baby_num

        # Write the current month's data in CSV format
        megalodons_file.write(f"{month},{adult_num},{baby_num},{meg_total}\n")

    # Write the month when sustenance will run out
    megalodons_file.write(f"\n--Sustenance will run out in month {month}\n")

    # Close the file
    megalodons_file.close()


do_research()
