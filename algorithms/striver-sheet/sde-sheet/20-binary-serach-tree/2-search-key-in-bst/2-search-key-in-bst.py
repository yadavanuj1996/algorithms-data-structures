"""
Search in a Binary Search Tree

Problem Link:
https://leetcode.com/problems/search-in-a-binary-search-tree/description/

Statement
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.

Constraints:
- The number of nodes in the tree is in the range [1, 5000].
- 1 <= Node.val <= 10^7
- root is a binary search tree.
- 1 <= val <= 10^7
 
Test Case: ( we have to return root pointer in output)
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

"""


"""
Time Complexity: O(log N), since it's a binary search tree the search space gets reduced by half
Space Complexity: O(1),  
"""
"""
Important Point: In BST all elements on left of node are smaller and all elements on right are larger.
"""
# Definition f2or a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        
        while node:
            if node.val < val:
                node = node.right
            elif node.val > val:
                node = node.left
            else:
                break
        
        return node

        