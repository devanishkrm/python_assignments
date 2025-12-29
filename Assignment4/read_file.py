"""
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""

filepath = "sample.txt"
try:
    with open(filepath, "rt") as fh:
        print("Reading file content:")
        line_content = fh.readline()
        line = 1
        while line_content != "":
            print(f"Line {line}: {line_content}", end="")
            line_content = fh.readline()
            line += 1
except FileNotFoundError:
    print(f"Error: The file '{filepath}' was not found")
