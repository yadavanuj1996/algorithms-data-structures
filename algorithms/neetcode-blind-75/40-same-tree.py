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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def is_same_tree(fst_cur_node, scd_cur_node):

            if not fst_cur_node and not scd_cur_node:
                return True

            # if two nodes are not same return false
            if (not fst_cur_node and scd_cur_node) or (fst_cur_node and not scd_cur_node) or \
             not (fst_cur_node.val == scd_cur_node.val) :
                return False

            # left subtree visit
            left = is_same_tree(fst_cur_node.left, scd_cur_node.left)
            # right subtree visit
            if left:
                right = is_same_tree(fst_cur_node.right, scd_cur_node.right)

            return left and right

        return is_same_tree(p, q)
