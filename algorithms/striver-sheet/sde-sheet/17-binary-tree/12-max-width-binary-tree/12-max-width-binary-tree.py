"""
Maximum Width of Binary Tree

Problem Link:
https://leetcode.com/problems/maximum-width-of-binary-tree/

Statement:
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost 
non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary
tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

Constraints:
- The number of nodes in the tree is in the range [1, 3000].
- -100 <= Node.val <= 100

Test Case:
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

"""

"""
Time Complexity:    
Space Complexity: 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # node, s no
        # s_no if horizontal serial no of a node at current level i.e., if all nodes are filled at current
        # level and we move from left to right (starting from 0) what will be the s_no of current node
        queue = deque([(root, 0)])
        res = 0
        
        while queue:
            min_s_no, max_s_no = None, None
            size = len(queue)       # represent no of nodes at current level
            for _ in range(size):
                cur_node, s_no = queue.popleft()
                
                min_s_no = s_no if (min_s_no is None) or (s_no < min_s_no) else min_s_no
                max_s_no = s_no if (max_s_no is None) or (s_no > max_s_no) else max_s_no
                
                if cur_node.left:
                    queue.append((cur_node.left, s_no * 2))

                if cur_node.right:
                    queue.append((cur_node.right, s_no * 2 + 1))
        
            
            level_res = max_s_no - min_s_no + 1
            res = max(res, level_res)

        return res
            

        