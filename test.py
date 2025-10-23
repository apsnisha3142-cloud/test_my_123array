# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 18:27:34 2025

@author: hp
"""

import array as arr

# Create an array of signed integers ('i' type code)
my_array = arr.array('i', [10, 20, 30, 40, 50])

print("Original array:", my_array)

# Append an element to the end of the array
my_array.append(60)
print("Array after appending 60:", my_array)

# Insert an element at a specific index (index 2, value 25)
my_array.insert(2, 25)
print("Array after inserting 25 at index 2:", my_array)

# Remove an element by value
my_array.remove(40)
print("Array after removing 40:", my_array)

# Remove an element by index (removes the element at index 1)
removed_element = my_array.pop(1)
print(f"Array after popping element at index 1 (removed: {removed_element}):", my_array)

# Access an element by index
print("Element at index 0:", my_array[0])

# Get the length of the array
print("Length of the array:", len(my_array))