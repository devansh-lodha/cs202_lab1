# This file is for demonstrating a pylint workflow.

import sys
import os

# Intentionally bad variable name and lack of docstrings
def myFunction(data):
    
    Temp_List = []
    for i in data:
        if i % 2 == 0:
            Temp_List.append(i * 2)
        else:
            Temp_List.append(i * 3)
    return Temp_List

def anotherFunction(n):
    if n < 0:
        print("Number must be non-negative.")
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return anotherFunction(n-1) + anotherFunction(n-2)


# A long line to trigger a line-too-long warning from pylint which is configured to check for lines longer than 80 characters by default.
long_variable_name_for_demonstration = "This is a very long string that is designed to exceed the eighty character limit that is standard in many Python style guides."

MyData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


TransformedData = myFunction(MyData)
print("Transformed Data:", TransformedData)

fib_number = 10
fib_result = anotherFunction(fib_number)
print(f"The {fib_number}th Fibonacci number is: {fib_result}")