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
Time Complexity: O(N),  actually O(2N) - O(n) for inorder traversal and o(n) for looping over the res
Space complexity: O(N), again O(2N) - O(n) for recursion stack and O(n) for storing in order result
Space Complexity: 

We have used the logic that if we run a inorder traversal on BST it returns an sorted array, so we 
simply have run the in order traversal on the given binary tree and checked if it's sorted or not
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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









