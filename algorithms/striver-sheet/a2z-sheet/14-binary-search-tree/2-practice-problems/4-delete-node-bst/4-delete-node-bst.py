"""
Delete Node in a BST

Problem Link:
https://leetcode.com/problems/delete-node-in-a-bst/description/

Statement
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.


Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- Each node has a unique value.
- root is a valid binary search tree.
- -10^5 <= key <= 10^5

Test Case:

Input: root = [5,3,6,2,4,null,7], key = 3

Output: [5,4,6,2,null,null,7]

Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

"""


"""
Time Complexity: O(log n), for balanced bst and for a skewed BST  o(n)
Space Complexity: O(log n), recursion stack or auxiliary space
""" 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def find_min_val_bst(node):
            while node.left:
                node = node.left
            
            return node

        def delete_node_bst(cur_node, key):
            if not cur_node:
                return None

            if key < cur_node.val:
                cur_node.left = delete_node_bst(cur_node.left, key)
            elif key > cur_node.val:
                cur_node.right = delete_node_bst(cur_node.right, key)
            # key == cur node val
            else:
                # The below two cases will handle a bst node that has 0 or 1 children
                if not cur_node.left:
                    return cur_node.right
                elif not cur_node.right:
                    return cur_node.left
                
                # Case where node has 2 childrens
                temp = find_min_val_bst(cur_node.right)
                cur_node.val = temp.val
                cur_node.right = delete_node_bst(cur_node.right, temp.val)
            
            return cur_node
            
        root = delete_node_bst(root, key)
        return root

        