"""
Left View of Binary Tree

Problem Link:
https://www.geeksforgeeks.org/problems/left-view-of-binary-tree/1

Statement
Given a Binary Tree, return Left view of it. Left view of a Binary Tree is set of nodes visible when 
tree is visited from Left side. The task is to complete the function leftView(), which accepts root of 
the tree as argument. If no left view is possible, return an empty tree.

Note:
All the nodes are zero-based.

Constraints:
0 <= Number of nodes <= 100
0 <= Data of a node <= 1000


Test Case:

Sample Input 1
1 2 3 N N 4 6 N 5 N N 7 N

Sample Output 1
1 2 4 5 7

"""

"""
Time Complexity: O(n), As the recursive fn will be called for each node, n is total no of nodes
Space Complexity: O(h), h is height of binary tree

Note: Although the recursion call is being made for each node the recursion stack at once will in
max case hold from root node to longest leaf node path that is height of tree thus SC is O(h)

Note: Not considering res space complexity as we do not generally add it as we are just returning
the answer using that data structure
"""

"""
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

from collections import deque

def LeftView(root):
    # code here

    # recursive fn that will work in O(h) space complexity
    def left_view(res, cur_node=root, cur_level=0):
        if cur_node is None:
            return
    
        if cur_level == len(res):
            res.append(cur_node.data)
    
        # call left child
        left_view(res, cur_node.left, cur_level+1)
        # call right child
        left_view(res, cur_node.right, cur_level+1)
        
        
    res = []
    left_view(res)
    return res
    
    