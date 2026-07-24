"""
TC: O(n^2)
SC: O(n^2)
"""
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Simple fn that returns index of element in an list
        def search_element_in_arr(arr, val):
            for i in range(len(arr)):
                if arr[i] == val:
                    return i

            return -1

        def build_binary_tree(pre_order_arr, in_order_arr):
            # Base cases
            if len(pre_order_arr) == 0:
                return None
            elif len(pre_order_arr) == 1:
                return TreeNode(pre_order_arr[0])

            root_val = pre_order_arr[0]
            root_in_order_index = search_element_in_arr(in_order_arr, root_val)
            # building left and right subtree in order traversal arr
            left_in_order_tree = in_order_arr[0:root_in_order_index]
            right_in_order_tree = in_order_arr[root_in_order_index+1:]
            # total count of left subtree nodes
            left_subtree_node_count = len(left_in_order_tree)
            # building left and right subtree in pre order traversal arr
            left_pre_order_tree = pre_order_arr[1 : 1+left_subtree_node_count]
            right_pre_order_tree = pre_order_arr[1+left_subtree_node_count : ]
            # Creating root node and setting up left and right node using recursive call of fn
            root_node = TreeNode(root_val)
            root_node.left = build_binary_tree(left_pre_order_tree, left_in_order_tree)
            root_node.right = build_binary_tree(right_pre_order_tree, right_in_order_tree)
            # returning the root node
            return root_node

        return build_binary_tree(preorder, inorder)
