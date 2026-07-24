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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float("-inf")]
        def path_sum_in_order(cur_node):
            if not cur_node:
                return 0

            cur_sum = cur_node.val
            left_sum = path_sum_in_order(cur_node.left)
            right_sum = path_sum_in_order(cur_node.right)

            if left_sum < 0:
                left_sum = 0

            if right_sum < 0:
                right_sum = 0

            max_sum[0] = max(max_sum[0], cur_sum+left_sum+right_sum)


            return max(cur_sum+left_sum, cur_sum+right_sum)

        path_sum_in_order(root)
        return max_sum[0]
