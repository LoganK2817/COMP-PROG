
from .. import artifact as ark
import pandas as pd
from pathlib import Path

write_outfile = True

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
    

    
    cell_num = 1
    list_number = 0
    
    cells = []
    
    for item in file.loc[:,:].to_numpy().flatten():
        if str(item) != "nan":
            out_file.write(f"{str(item)} --CELL-- {cell_num} --LIST-- {list_number}\n")
            cells.append(str(item))
            cell_num += 1
            list_number += 1
        
    # print(cells)
    
    out_dataframe_info = {"Day": [cells[0],cells[5]],
                          "Position": [cells[1],cells[6]],
                          "In": [cells[2],cells[7]]}
    out_dataframe = pd.DataFrame(data=out_dataframe_info)
    print(out_dataframe)
    
    
    #-----------------------------------------------------------------------
    ark.br(40)
    if write_outfile:
        # out_file.write(str(file.head()))
        out_file.close()
    
    
    
    
    
    
    
    
    
main()