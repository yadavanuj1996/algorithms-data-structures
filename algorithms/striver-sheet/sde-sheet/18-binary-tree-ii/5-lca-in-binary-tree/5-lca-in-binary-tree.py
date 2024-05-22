"""
Lowest Common Ancestor of a Binary Tree

Problem Link:
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Statement
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two 
nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to 
be a descendant of itself).”

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the tree.


Test Case:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

"""

"""
Time Complexity: O(n), As the recursive fn will be called for each node, n is total no of nodes
Space Complexity: O(h), auxiliary stack space h is height of binary tree

In worst case skewed tree will have height = n then space complexity will become O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def get_lca(cur_node, p , q):
            # base case
            if cur_node == p or cur_node == q or cur_node == None:
                return cur_node
            
            left = get_lca(cur_node.left, p, q)
            right = get_lca(cur_node.right, p, q)

            if left and right:
                return cur_node
            elif left and not right:
                return left
            elif not left and right:
                return right
            
        return get_lca(root, p, q)
                
        