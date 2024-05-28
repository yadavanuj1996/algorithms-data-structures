"""
Binary Tree Zigzag Level Order Traversal

Problem Link:
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Statement
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -100 <= Node.val <= 100


Test Case:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: 
            return None
        
        # root, cur horizontal level 
        queue = deque([root])
        is_left_to_right = True
        res = []
    
        while queue:
            size = len(queue)
            res_row = [0] * size
            
            for i in range(size):
                cur_node = queue.popleft()
                
                index = i if is_left_to_right else size-i-1
                res_row[index] = cur_node.val

                if cur_node.left:
                    queue.append(cur_node.left)
                
                if cur_node.right:
                    queue.append(cur_node.right)

            # adding res row to actual res
            res.append(res_row)     
            # flipping the boolean flag depending as alternate levels direction will change
            is_left_to_right = not is_left_to_right
            
        return res



        