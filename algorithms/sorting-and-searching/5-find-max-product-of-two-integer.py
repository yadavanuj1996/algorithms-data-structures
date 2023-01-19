"""
Problem statement
Implement a function find_max_prod(lst) that takes a list of numbers and returns a maximum product pair.

Input
A list of integer numbers

Output
Two integers
"""

# Decimal library to assign infinite numbers
from decimal import Decimal


def find_max_prod(lst):
    """
    Solution in O(n) to find max 2 and min 2 elements of array (for -ve numbers) and comparing their product 
    """
    if not lst:
        return False

    min_2 = float('-inf')
    min_1 = lst [0]
    max_2= float('inf')
    max_1 = lst[0]

    for item in lst:
        if item >= max_1:
            max_2 = max_1
            max_1 = item
        
        if item <= min_1:
            min_2 = min_1
            min_1 = item
    
    if max_2 * max_1 > min_1 * min_2:
        return (max_2, max_1)
    else:
        return (min_2, min_1)
    
    # Write your code here!
    