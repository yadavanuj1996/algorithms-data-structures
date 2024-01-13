"""
Ceil from BST

Problem Link:
https://www.codingninjas.com/studio/problems/ceil-from-bst_920464?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

Statement
Ninja is given a binary search tree and an integer. Now he is given a particular key in the tree and returns its ceil value. Can you help Ninja solve the problem?

Note:
Ceil of an integer is the closest integer greater than or equal to a given number.
For example:
arr[] = {1, 2, 5, 7, 8, 9}, key = 3.
The closest integer greater than 3 in the given array is 5. So, its ceil value in the given array is 5.

Constraints:
- 1 <= T <= 10    
- 1 <= N <= 10^5
- 0 <= node data <= 10^9
- 1 <= X <= 10^9     

Test Case:

Input:
2
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
4
8 5 10 2 6 -1 -1 -1 -1 -1 7 -1 -1
7

Output:
5
7

"""


"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""
from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the TreeNode class structure

    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
'''

def findCeil(root, x):
    ceil = -1

    node = root
    while node:
        if node.data == x:
            ceil = node.data
            return ceil
        
        if node.data > x:
            ceil = node.data
            node = node.left
        else:
            node = node.right
    
    return ceil
            
        

            















