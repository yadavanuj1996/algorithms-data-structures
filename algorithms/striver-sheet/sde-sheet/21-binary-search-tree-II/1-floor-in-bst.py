"""
Floor in BST

Problem Link:
https://www.codingninjas.com/studio/problems/floor-from-bst_920457?source=youtube&campaign=Striver_Tree_Videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=Striver_Tree_Videos&leftPanelTabValue=PROBLEM

Statement
You are given a BST (Binary search tree) with’ N’ number of nodes and a value ‘X’. Your task is to find
the greatest value node of the BST which is smaller than or equal to ‘X’.

Constraints:
- 1 <= T <= 5
- 1 <= N <= 5 * 10^3
- 1 <= nodeVal[i] <= 10^9
 
Test Cases:

Input:
2
10 5 15 2 6 -1 -1 -1 -1 -1 -1
7
2 1 3 -1 -1 -1 -1
2

Output:
6
2

"""


"""
Time Complexity: O(H) , h is height of tree, for a balanced BST it will be O(log n)
Space Complexity: O(1)
"""
from os import *
from sys import *
from collections import *
from math import *
"""
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    Following is the TreeNode class structure

    class TreeNode:

        def __init__ (self, data):

            self.data = data
            self.left = None
            self.right = None
            
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""

def floorInBST(root, X):

    def floor_in_bst(node, floor):
        if not node:
            return floor
            
        if node.data > X:
            return floor_in_bst(node.left, floor)            
        elif node.data < X:
            floor = node.data
            return floor_in_bst(node.right, floor)
        else:
            floor = node.data      
            return floor              

    return floor_in_bst(root, -1)



