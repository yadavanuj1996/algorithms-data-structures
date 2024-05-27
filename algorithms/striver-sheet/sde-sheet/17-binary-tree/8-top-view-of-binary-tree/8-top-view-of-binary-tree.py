"""
Top View of Binary Tree

Problem Link:
https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1

Statement
Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary 
tree is the set of nodes visible when the tree is viewed from the top.

For ex - 
1 2 3 N 4 5 N 6 N 7 N 8 N 9 N N N N N will give 8 2 1 3 as answer.

Constraints:
- 1 ≤ N ≤ 10^5
- 1 ≤ Node Data ≤ 10^5


Test Case:

Sample Input 1
10 20 30 40 60 90 100

Sample Output 1
40 20 10 30 100

"""

"""
Time Complexity: O(N),
Space Complexity: O(N) , We are using queue and dict

Note: Although the recursion call is being made for each node the recursion stack at once will in
max case hold from root node to longest leaf node path that is height of tree thus SC is O(h)

Note: Not considering res space complexity as we do not generally add it as we are just returning
the answer using that data structure
"""

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
from collections import deque
class Solution:
    def topView(self,root):
        queue = deque()
        result_dict = {}
        
        # (cur_node, vertical line number) 
        queue.append((root, 0))
        
        while queue:
            cur_node, line = queue.popleft()
            
            # if there exists already an node for a key line means a node which is on top
            # is already above this node looking from top view
            if line not in result_dict:
                # key=vertical line number, value = node value
                result_dict[line] = cur_node.data    
            
            
            
            # if we move left then vertival line is decreased by 1
            if cur_node.left:
                queue.append((cur_node.left, line-1))
                
            # if we move left then vertival line is increased by 1
            if cur_node.right:
                queue.append((cur_node.right, line+1))
                
        res = []
        for item in sorted(result_dict):
            res.append(result_dict[item])
        
        return res
        
            
            
        