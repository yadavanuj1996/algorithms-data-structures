from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Time Complexity: O(N),  actually O(2N) - O(n) for inorder traversal and o(n) for looping over the res
Space complexity: O(N), again O(2N) - O(n) for recursion stack and O(n) for storing in order result
Space Complexity:

We have used the logic that if we run a inorder traversal on BST it returns an sorted array, so we
simply have run the in order traversal on the given binary tree and checked if it's sorted or not
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def get_valid_bst(node, min_limit, max_limit):
            if not node:
               return True

            if min_limit < node.val and node.val < max_limit:
                left_tree_res = get_valid_bst(node.left, min_limit, node.val)
                right_tree_res = get_valid_bst(node.right, node.val, max_limit)
                return left_tree_res and right_tree_res
            else:
                return False

        return get_valid_bst(root, float("-inf"), float("inf"))
