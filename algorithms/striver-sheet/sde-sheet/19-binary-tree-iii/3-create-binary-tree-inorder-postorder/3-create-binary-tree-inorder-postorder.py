"""
Construct Binary Tree from Inorder and Postorder Traversal

Problem Link:
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Statement
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree 
and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Constraints:
- 1 <= inorder.length <= 3000
- postorder.length == inorder.length
- -3000 <= inorder[i], postorder[i] <= 3000
- inorder and postorder consist of unique values.
- Each value of postorder also appears in inorder.
- inorder is guaranteed to be the inorder traversal of the tree.
- postorder is guaranteed to be the postorder traversal of the tree.


Test Case:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Input: inorder = [-1], postorder = [-1]
Output: [-1]

"""


"""
Solution 1:
Time Complexity: O(N^2)
Space Complexity: o(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def build_tree(in_order:List[int], post_order:List[int]):
            if len(in_order) == 0:
                return None
            
            cur_root = TreeNode(val=post_order[-1])
            cur_root_in_order_index = in_order.index(cur_root.val)
            
            # left child creation
            cur_root.left = build_tree(in_order[0:cur_root_in_order_index], post_order[0:cur_root_in_order_index])
            # right child creation
            cur_root.right = build_tree(in_order[cur_root_in_order_index+1:], post_order[cur_root_in_order_index:-1])

            return cur_root

        return build_tree(inorder, postorder)


        