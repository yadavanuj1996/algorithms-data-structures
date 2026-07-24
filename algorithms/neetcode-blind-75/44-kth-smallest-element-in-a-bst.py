"""
TC: O(n)
SC: O(n)
"""
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def pre_order_traversal(node, res=[]):
            if not node:
                return

            pre_order_traversal(node.left, res)
            res.append(node.val)
            pre_order_traversal(node.right, res)

            return res

        res =  pre_order_traversal(root)
        return res[k-1]
