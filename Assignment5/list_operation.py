import copy

"""
Task 2: Demonstrate List Slicing
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

"""

initial_list = [1,2,3,4,5,6,7,8,9,10]
extracted_list = initial_list[0:5]
reverse_list = copy.copy(extracted_list)
reverse_list.reverse()

print(f"Original list: {initial_list}")
print(f"Extracted first five elements: {extracted_list}")
print(f"Reversed extracted elements: {reverse_list}")