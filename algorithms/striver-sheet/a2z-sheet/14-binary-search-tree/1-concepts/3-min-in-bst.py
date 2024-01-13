"""
Minimum element in BST

Problem Link:
https://www.codingninjas.com/studio/problems/minimum-element-in-bst_8160462?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

Statement
You are given a Binary Search Tree. Find the minimum value in it.

Note: All the values in the given binary search tree are unique.

Constraints:
- 0 <= ‘n’ <= 10^5
- Time Limit: 1 sec

Test Case:

Input : 6 4 7 2 5 N N

Output: 2
"""


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''

def minVal(root):
    # Write your code here.
    if not root:
        return -1
        
    node = root
    while node.left:
        node = node.left
    
    return node.data