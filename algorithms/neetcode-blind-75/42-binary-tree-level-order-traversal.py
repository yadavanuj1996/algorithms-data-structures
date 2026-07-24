"""
TC: O(n)
SC: O(n)
"""
from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque([(root, 0)])

        while queue:
            cur_node, cur_level = queue.popleft()

            if not cur_node:
                continue

            if len(res) <= cur_level:
                res.append([])

            res[cur_level].append(cur_node.val)

            # add left child to queue
            queue.append((cur_node.left, cur_level+1))
            # add right child to queue
            queue.append((cur_node.right, cur_level+1))

        return res
