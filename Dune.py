"""
Name: Logan

Description:
This program reads a scrambled data file (`planet_data.txt`) that contains interleaved lines from three text files
about the planet Arrakis: ecology (ECO), sandworms (WRM), and spice (SPC). Each line is labeled with a line number
and a 3-letter code. The program unscrambles the lines into three correct files, writes the cleaned-up text to
`holo_data.txt`, and generates a summary in `holo_summary.txt` containing the longest, shortest, and average line
length for each file type.

Resources Used:
None beyond Python documentation.

Difficulties:
Carefully tracking the correct line number and line lengths while sorting and removing metadata was a bit tricky,
but manageable.
"""

import sys

def parse_file(filename):
    file_data = {'ECO': [], 'WRM': [], 'SPC': []}

    with open(filename, 'r') as f:
        for line in f:
            text, line_num, code = line.strip().rsplit('|', 2)
            line_num = int(line_num)
            file_data[code].append((line_num, text))

    return file_data

def write_holo_data(file_data):
    with open('holo_data.txt', 'w') as f:
        for code in ['ECO', 'SPC', 'WRM']:
            f.write(f'{code}\n')
            f.write('-' * 24 + '\n\n')
            sorted_lines = sorted(file_data[code])
            for _, text in sorted_lines:
                f.write(f'{text}\n')
            f.write('\n')

def compute_summary(file_data):
    summary = {}
    for code in ['ECO', 'SPC', 'WRM']:
        sorted_lines = sorted(file_data[code])
        lengths = [(len(text), line_num, text) for line_num, text in sorted_lines]
        total_len = sum(length for length, _, _ in lengths)
        avg_len = round(total_len / len(lengths))

        # Get shortest and longest by line length, then line number
        shortest = min(lengths, key=lambda x: (x[0], x[1]))
        longest = max(lengths, key=lambda x: (x[0], -x[1]))

        summary[code] = {
            'shortest': (shortest[2], shortest[1]),
            'longest': (longest[2], longest[1]),
            'average': avg_len
        }

    return summary

def write_summary(summary):
    with open('holo_summary.txt', 'w') as f:
        for code in ['ECO', 'SPC', 'WRM']:
            f.write(f'{code} SUMMARY\n')
            f.write('-' * 24 + '\n')
            f.write(f'Longest line ({summary[code]["longest"][1]}): {summary[code]["longest"][0]}\n')
            f.write(f'Shortest line ({summary[code]["shortest"][1]}): {summary[code]["shortest"][0]}\n')
            f.write(f'Average line length: {summary[code]["average"]}\n\n')

def main():
    if len(sys.argv) < 2:
        print("Usage: python unscramble.py planet_data.txt")
        return

    filename = sys.argv[1]
    file_data = parse_file(filename)
    write_holo_data(file_data)
    summary = compute_summary(file_data)
    write_summary(summary)
    print("holo_data.txt and holo_summary.txt have been written successfully.")

if __name__ == '__main__':
    main()
