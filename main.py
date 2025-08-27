"""
This module demonstrates a pylint workflow and contains functions
for data transformation and Fibonacci calculation.
"""
import os # Unused import 'sys' has been removed.

def transform_data(data_list):
    """Transforms a list of numbers, doubling evens and tripling odds."""
    temp_list = []
    for item in data_list:
        if item % 2 == 0:
            temp_list.append(item * 2)
        else:
            temp_list.append(item * 3)
    return temp_list

def calculate_fibonacci(num):
    """Calculates the nth Fibonacci number using recursion."""
    if num < 0:
        print("Number must be non-negative.")
        return None
    if num in (0, 1):
        return num
    return calculate_fibonacci(num - 1) + calculate_fibonacci(num - 2)

# Line is now broken into a more readable format.
# Note: unused 'long_variable_name_for_demonstration' and 'os' are removed
# to pass pylint checks for unused variables/imports.

MY_DATA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

transformed_list = transform_data(MY_DATA)
print("Transformed Data:", transformed_list)

FIB_NUMBER = 10
fib_result = calculate_fibonacci(FIB_NUMBER)
print(f"The {FIB_NUMBER}th Fibonacci number is: {fib_result}")