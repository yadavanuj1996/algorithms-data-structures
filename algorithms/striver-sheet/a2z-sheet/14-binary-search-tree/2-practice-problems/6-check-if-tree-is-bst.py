"""
Validate Binary Search Tree

Problem Link:
https://leetcode.com/problems/validate-binary-search-tree/description/

Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1


Test Case:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""


"""
Solution 1
Time Complexity: O(N),  actually O(2N) - O(n) for inorder traversal and o(n) for looping over the res
Space complexity: O(N), again O(2N) - O(n) for recursion stack and O(n) for storing in order result


We have used the logic that if we run a inorder traversal on BST it returns an sorted array, so we 
simply have run the in order traversal on the given binary tree and checked if it's sorted or not
Also N is total no of elements, not the height (IMP)



class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def get_inorder_traversal(node):
            if not node:
                return 

            get_inorder_traversal(node.left)
            res.append(node.val)
            get_inorder_traversal(node.right)
        
        get_inorder_traversal(root)

        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        
        return True

"""




"""
Solution 2
Time Complexity: O(N),  actually O(2N) - O(n) for inorder traversal and o(n) for looping over the res
Space complexity: O(N), again O(2N) - O(n) for recursion stack and O(n) for storing in order result

This solution is better than above as we are not using res array thus the space complexity though linear in 
both case it's better for solution no 2 (below solution).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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














