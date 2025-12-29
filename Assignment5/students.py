"""
Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""

students = {
    "john" : 90,
    "kumar" : 80,
    "anish" : 89,
    "amal" : 67,
    "sam": 97
}

search = input("Enter student's name: ")
search_key = search.lower()

if students.get(search_key) is not None:
    print(f"{search}'s marks: {students[search_key]}")
else:
    print("Student not found.")
