src_file = open("SEM 2/misc files/planet_data.txt", "r")
sorted_file = open("SEM 2/misc files/sorted_data.txt", "w")

wrm_lines = []

for line in src_file:
    if line.find("ECO") == -1:
        print("Error")
    else:
        wrm_lines.append(line)


# Define a function to extract the line number for sorting
def extract_line_number(line):
    # Split by '|' to isolate the line number (e.g., |30|WRM -> 30)
    parts = line.split("|")
    return int(parts[1])  # Convert the line number to an integer

# Sort the list of WRM lines based on their line numbers
sorted_wrm_lines = sorted(wrm_lines, key=extract_line_number)

# Write the sorted lines to the output file
for sorted_line in sorted_wrm_lines:
    sorted_file.write(sorted_line)

# Close the files
src_file.close()
sorted_file.close()