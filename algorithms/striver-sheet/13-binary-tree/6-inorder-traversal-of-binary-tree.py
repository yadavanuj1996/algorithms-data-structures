"""
Problem Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inOrder(root, [])
        
    def inOrder(self, root: Optional[TreeNode], result: List[int]):
        if not root:
            return
        
        self.inOrder(root.left, result)
        result.append(root.val)
        self.inOrder(root.right, result)
        return result