"""
TC: O(n)
SC: O(h) recursion stack
"""
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def get_height(cur_node):
            if not cur_node:
                return 0

            left_subtree_height = get_height(cur_node.left)
            right_subtree_height = get_height(cur_node.right)

            return 1 + max(left_subtree_height, right_subtree_height)

        return get_height(root)
