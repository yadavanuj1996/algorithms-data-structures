"""
Balanced Binary Tree

Problem Link:
https://leetcode.com/problems/balanced-binary-tree/

Statement
Given a binary tree, determine if it is height-balanced.



Constraints:
- The number of nodes in the tree is in the range [0, 5000].
- -10^4 <= Node.val <= 10^4


Test Case:

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

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

"""
Three Conditions to check if BT is height balanced
1. difference between the left and the right subtree for any node is not more than one
2. the left subtree is balanced
3. the right subtree is balanced
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def get_height(cur_node):
            if not cur_node:
                return 0
            
            left_height = get_height(cur_node.left)

            if left_height == -1:
                return -1

            right_height = get_height(cur_node.right)
            if right_height == -1:
                return -1

            # if the abs height difference between left and subtree is 0 or 1 then it's height 
            # balanced binary tree
            if abs(left_height - right_height) > 1:
                return -1
        
            return 1 + max(left_height, right_height)
        
        if get_height(root) == -1:
            return False
            
        return True
            
        
        