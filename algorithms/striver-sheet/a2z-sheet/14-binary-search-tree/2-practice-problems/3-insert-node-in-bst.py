"""
Insert into a Binary Search Tree


Problem Link:
https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

Statement
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Constraints:
- 1 <= T <= 10    
- 1 <= N <= 10^5
- 0 <= node data <= 10^9
- 1 <= X <= 10^9     

Test Case:

Input:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

"""


"""
Time Complexity: O(log n)
Space Complexity: O(1)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        # To handle the case where root is null, no bst exists yet
        if not node:
            root = TreeNode(val)

        while node:
            if node.val < val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    node = node.right
                    break
            else:
                if node.val > val:
                    if node.left:
                        node = node.left
                    else:
                        node.left = TreeNode(val)
                        node = node.left
                        break
        
        return root


        