"""
TC: O(h)
SC: O(h) recursion stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
