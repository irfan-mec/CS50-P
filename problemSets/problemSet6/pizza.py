import sys
import os
import csv
from tabulate import tabulate

def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            table = [row for row in reader]
        return table
    except FileNotFoundError:
        sys.exit(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        sys.exit(f"Error: {e}")

if len(sys.argv) != 2:
    sys.exit("Usage: python pizza.py <filename.csv>")

file_name = sys.argv[1]

# Check if the file has a .csv extension
if not file_name.endswith(".csv"):
    sys.exit("Error: File must have a .csv extension.")

# Check if the file exists
if not os.path.isfile(file_name):
    sys.exit(f"Error: File '{file_name}' not found.")

# Read the CSV file
table = read_csv(file_name)

# Output the table as ASCII art using grid format
print(tabulate(table, headers="firstrow", tablefmt="grid"))