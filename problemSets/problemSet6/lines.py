import sys
import os

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        code_lines = 0
        for line in lines:
            stripped_line = line.strip()
            # Ignore blank lines and comment lines
            if stripped_line and not stripped_line.startswith("#"):
                code_lines += 1

        return code_lines
    except FileNotFoundError:
        sys.exit(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        sys.exit(f"Error: {e}")

if len(sys.argv) != 2:
    sys.exit("Usage: python lines.py <filename.py>")

file_name = sys.argv[1]

# Check if the file has a .py extension
if not file_name.endswith(".py"):
    sys.exit("Error: File must have a .py extension.")

# Check if the file exists
if not os.path.isfile(file_name):
    sys.exit(f"Error: File '{file_name}' not found.")

# Count lines of code
lines_of_code = count_lines(file_name)
print(f"Lines of code: {lines_of_code}")