"""
Symmetric Tree

Problem Link:
https://leetcode.com/problems/symmetric-tree/

Statement
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around
its center).

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- -100 <= Node.val <= 100


Test Case:
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
"""

"""
Time Complexity: O(N) , no of nodes
Space Complexity: O(h), H height of tree worst case O(n) skewed tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_symmetric(left_node, right_node):
            # we are checking if nodes or values don't match then return False else keep looking for other nodes
            if not left_node or not right_node:
                return left_node == right_node

            if not left_node.val == right_node.val:
                return False

            return is_symmetric(left_node.left, right_node.right) and is_symmetric(left_node.right, right_node.left)  
        

        return is_symmetric(root.left, root.right)





            
        
