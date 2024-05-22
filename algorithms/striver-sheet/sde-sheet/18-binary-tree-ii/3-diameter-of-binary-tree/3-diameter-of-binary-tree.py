"""
Diameter of Binary Tree

Problem Link:
https://leetcode.com/problems/diameter-of-binary-tree/

Statement
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.


Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -100 <= Node.val <= 100


Test Case:

Example 1:
Input: root = [1,2,3,4,5]
Output: 3

Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

"""

"""
Time Complexity: O(n), As the recursive fn will be called for each node, n is total no of nodes
Space Complexity: O(h), auxiliary stack space h is height of binary tree

In worst case skewed tree will have height = n then space complexity will become O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = [0]

        # get height fn that calculate max left subtree height and max right subtree height with a
        # twist of adding one line to calculate max of diameter and cur diameter, diameter is no of edges
        # between two node i.e., height of left subtree + height of right subtree
        def get_height(cur_node):
            if not cur_node: 
                return 0

            # left subtree max height
            left_height = get_height(cur_node.left)
            # right subtree max height
            right_height = get_height(cur_node.right)

            max_dia[0] = max(max_dia[0], left_height+right_height)

            return 1 + max(left_height, right_height)
        
        # call get_height fn to store left and right subtree max height of each node
        get_height(root)

        return max_dia[0]

