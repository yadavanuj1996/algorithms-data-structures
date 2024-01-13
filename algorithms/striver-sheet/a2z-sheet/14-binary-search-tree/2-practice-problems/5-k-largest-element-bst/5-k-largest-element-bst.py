"""
Kth Smallest Element in a BST

Problem Link:
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

Statement
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all
the values of the nodes in the tree.

Constraints:
- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4  

Test Case:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

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
    
    
        
        





