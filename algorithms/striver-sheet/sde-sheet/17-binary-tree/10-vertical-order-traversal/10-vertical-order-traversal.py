"""
Vertical Order Traversal of a Binary Tree

Problem Link:
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

Statement:
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions 
(row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each 
column index starting from the leftmost column and ending on the rightmost column. There may 
be multiple nodes in the same row and same column. In such a case, sort these nodes by their 
values.

Return the vertical order traversal of the binary tree.

Constraints:
- The number of nodes in the tree is in the range [1, 1000].
- 0 <= Node.val <= 1000

Test Case:
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.

Example 2:

Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]

Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.

"""

"""
Time Complexity: O(N) + O (K log K), k is no of vertical lines (worst case N)
Space Complexity: O(N) , We are using queue and dict

Note: Although the recursion call is being made for each node the recursion stack at once will in
max case hold from root node to longest leaf node path that is height of tree thus SC is O(h)

Note: Not considering res space complexity as we do not generally add it as we are just returning
the answer using that data structure
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        res_dict = {}
        queue = deque([(root,0)])
        
        while queue:
            size = len(queue)
            row_dict = {} # will hold result for a particular level
                 
            for i in range(size):
                cur_node, ver_level = queue.popleft()

                if not row_dict.get(ver_level):
                    row_dict[ver_level] = [cur_node.val]
                    if not res_dict.get(ver_level):
                        res_dict[ver_level] = []
                else:
                    row_dict[ver_level].append(cur_node.val)
                
                if cur_node.left:
                    queue.append((cur_node.left, ver_level-1))
                
                if cur_node.right:
                    queue.append((cur_node.right, ver_level+1))
        
            for key in row_dict:
                if len(row_dict[key]) > 1:
                    row_dict[key] = sorted(row_dict[key])
                res_dict[key] += row_dict[key]

        res = []
        
        for key in sorted(res_dict):
            res.append((res_dict[key]))
        
        return res
