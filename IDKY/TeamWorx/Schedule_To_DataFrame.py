
from .. import artifact as ark
import pandas as pd
from pathlib import Path

write_outfile = False

out_file_location = Path("IDKY") / "TeamWorx" / "outSchedule.txt"
if write_outfile:
    out_file = open(out_file_location, "w")
    
    
def main():
        # locate and determine file with variable
    file_location = Path("IDKY") / "TeamWorx" /"MySchedule_Jan26_Feb01.xlsx"
    file = pd.read_excel(file_location,header=4) # Turns the excel sheet into a dataframe
        # trim the unneeded shit 
    file = file.loc[:, ~file.columns.str.contains("^Unnamed")]
    file = file.drop([0])
    # file = file.drop_duplicates("Out")
    
    file.columns = ["Position", "In", "Out", "Hours"]
    # file.index = ["Shift1 Date","Shift1 Details","Shift2 Date","Shift2 Details"]
    ark.br(40)
    #-----------------------------------------------------------------------
    
    row = 1
    column = 0
    
    # for item in file.loc[:,file.columns[column]]:
    #     for item in file.loc[row,:]:
    #         print(item, type(item))
    #         row += 1
    #         print("row",row)
    #     print("column",column)
    #     column += 1
    
    print(file.loc[1:2, "Position":"In"])
    ark.br(20)
    for value in file.loc[1:2, "Position":"In"].to_numpy().flatten():
        print(value)

    
    
    #-----------------------------------------------------------------------
    ark.br(40)
    if write_outfile:
        out_file.write(str(file.head()))
        out_file.close()
    
    
    
    
    
    
    
    
    
main()