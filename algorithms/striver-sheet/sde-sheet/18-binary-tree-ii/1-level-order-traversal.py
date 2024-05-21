"""
Binary Tree Level Order Traversal

Problem Link:
https://leetcode.com/problems/binary-tree-level-order-traversal/

Statement
Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100


Test Case:

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

"""
Time Complexity: O(n), 
Space Complexity: O(n), all nodes will be added to queue
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque([(root, 0)])
        
        while queue:
            cur_node, cur_level = queue.popleft()
            
            if not cur_node:
                continue

            while len(res) <= cur_level:
                res.append([])
            
            res[cur_level].append(cur_node.val)
        
            # add left child to queue
            queue.append((cur_node.left, cur_level+1))
            # add right child to queue
            queue.append((cur_node.right, cur_level+1))
        
        return res

        

        
        