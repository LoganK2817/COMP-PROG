import matplotlib.pyplot as plt
import re

def extract_coordinates(filename):
    with open(filename, 'r') as file:
        text = file.read()
    
    # Extract coordinates using regex
    coordinates = re.findall(r'\((-?\d+),\s*(-?\d+)\)', text)
    
    # Convert to list of tuples with integers
    return [(int(x), int(y)) for x, y in coordinates]

def plot_points(coordinates):
    x_vals, y_vals = zip(*coordinates)  # Unpack x and y values
    
    plt.figure(figsize=(10, 6))
    plt.scatter(x_vals, y_vals, color='blue', label='Points')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Plot of Points')
    plt.show()
    

def closePlot():
    plt.close()
    
def main():
    
    # Load and plot data
    filename = 'TLOF_Points.txt'
    coordinates = extract_coordinates(filename)
    plot_points(coordinates)

