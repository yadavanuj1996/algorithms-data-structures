"""
Binary Tree Maximum Path Sum

Problem Link:
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Statement
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence
has an edge connecting them. A node can only appear in the sequence at most once. Note that the 
path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.


Constraints:
- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -1000 <= Node.val <= 1000

Test Case:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
"""

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