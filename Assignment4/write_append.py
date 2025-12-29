"""
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
"""

filepath = "output.txt"

with open(filepath, "wt") as fh:
    text = input("Enter text to write to the file: ")
    fh.write(text)
    fh.write("\n")
    print(f"Data successfully written to {filepath}.")
    text = input("Enter additional text to append: ")
    fh.write(text)
    print("Data successfully appended.")

with open(filepath, "rt") as fh:
    print(f"Final content of {filepath}:")
    print(fh.read())
