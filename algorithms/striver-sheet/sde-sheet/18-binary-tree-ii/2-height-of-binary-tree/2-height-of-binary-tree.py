"""
Maximum Depth of Binary Tree

Problem Link:
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Statement
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to 
the farthest leaf node.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100


Test Case:

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

"""

"""
Time Complexity: O(n), As the recursive fn will be called for each node, n is total no of nodes
Space Complexity: O(h), h is height of binary tree

In worst case skewed tree will have height = n then space complexity will become O(n)
"""

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
        
    