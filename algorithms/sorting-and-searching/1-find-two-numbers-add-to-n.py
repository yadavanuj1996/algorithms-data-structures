# Challenge 1: Find Two Numbers that Add up to "n"
"""
Problem statement
In this problem, you have to implement the find_sum(lst, n) function which will take a list lst and number n as inputs and return two numbers from the list that add up to n.
Input
A list and a number n

Output
A list with two integers a and b that add up to n

Sample input
lst = [1, 21, 3, 14, 5, 60, 7, 6]
n = 81
Sample output
result = [21, 60]

"""
# Solution in O(n) time complexity using python set
def find_sum(lst, n):
    """
    Function to find two number that add up to n
    :param lst: A list of integers
    :param n: The integer number n
    """

    # Write your code here!
    found_item = set()

    for item in lst:
        if n-item in found_item:
            return [item, n-item]
        else:
            found_item.add(item)
    
    return False