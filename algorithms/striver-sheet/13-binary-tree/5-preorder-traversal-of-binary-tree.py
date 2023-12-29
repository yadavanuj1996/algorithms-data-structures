"""
Problem Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.preOrder(root, [])
    
    def preOrder(self, root: Optional[TreeNode], result: List[int]):
        if not root:
            return
        
        result.append(root.val)
        self.preOrder(root.left, result)
        self.preOrder(root.right, result)
        return result