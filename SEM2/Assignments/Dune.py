"""
Name: Logan Kunz
Project: Holo-book file unscrambler

Description:
Reads scrambled holo-book data from a file and separates it into sections based on source labels (ECO, WRM, SPC). 
Sorts the lines, writes a clean version of each section, and produces a summary with longest, shortest, and average line lengths.

Resources used:
- Python documentation
- ChatGPT guidance for new material

Challenges:
- Handling line splitting and sorting by line number
- Making sure longest/shortest tie-breaking used the lowest line number
"""




import sys

def parse_file(filename):
    file_data = {'ECO': [], 'WRM': [], 'SPC': []}

    with open(filename, 'r') as f:
        for line in f:
            text, line_num, code = line.strip().rsplit('|', 2)
            line_num = int(line_num)
            file_data[code].append((line_num, text))
    
    for code in file_data:
        file_data[code].sort()
    
    return file_data



def write_holo_data(file_data):
    with open('holo_data.txt', 'w') as f:
        for code in ['ECO', 'SPC', 'WRM']:  # write in this order
            f.write(f"{code}\n")
            f.write("-" * 24 + "\n")

            for line_num, text in file_data[code]:
                f.write(f"{text}\n")

            f.write("\n")  # extra line between sections


def write_summary(file_data):
    with open('holo_summary.txt', 'w') as f:
        for code in ['ECO', 'SPC', 'WRM']:
            lines = file_data[code]
            
            longest = shortest = lines[0]
            total_length = 0
            
            for line_num, text in lines:
                length = len(text)
                total_length += length
                
                if length > len(longest[1]) or (length == len(longest[1]) and line_num < longest[0]):
                    longest = (line_num, text)
                if length < len(shortest[1]) or (length == len(shortest[1]) and line_num < shortest[0]):
                    shortest = (line_num, text)

            avg_length = round(total_length / len(lines))

            f.write(f"{code} SUMMARY\n")
            f.write(f"Longest line ({longest[0]}): {longest[1]}\n")
            f.write(f"Shortest line ({shortest[0]}): {shortest[1]}\n")
            f.write(f"Average line length: {avg_length}\n\n")



def main():
    filename = sys.argv[1]
    data = parse_file(filename)
    write_holo_data(data)
    write_summary(data)
if __name__ == '__main__':
    main()
