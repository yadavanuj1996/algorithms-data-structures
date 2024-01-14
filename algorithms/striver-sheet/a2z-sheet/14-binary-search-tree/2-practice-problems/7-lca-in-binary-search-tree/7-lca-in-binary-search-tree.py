"""
Lowest Common Ancestor of a Binary Search Tree

Problem Link:
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Statement
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes
p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant
of itself).”

Constraints:
- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the BST    

Test Case:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

"""


"""
Time Complexity: O(H), H is height for balanced bst it will be O(log n), for non balanced O(n)
Space Complexity: O(H), H is height for balanced bst it will be O(log n), for non balanced O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Making sure that p contains small value than q
        if p.val > q.val:
            temp = p
            p = q
            q = temp

        def get_common_ancestor(node: "TreeNode"):
            if p.val < node.val and q.val < node.val:
                return get_common_ancestor(node.left)
            elif p.val > node.val and q.val > node.val:
                return get_common_ancestor(node.right)
            # The below 2 cases not checked both returns the node, thus we simply return the node
            # if p.val < node.val and node.val < q.val:
            # if p.val == node.val or q.val == node.val:
            return node
        
        return get_common_ancestor(root)
