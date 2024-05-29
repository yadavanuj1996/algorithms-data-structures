"""
Root to Leaf Paths

Problem Link:
https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1

Statement:
Given a Binary Tree of nodes, you need to find all the possible paths from the root node to 
all the leaf nodes of the binary tree.

Constraints:
- 1 ≤ N ≤ 10^4

Test Case:
Sample Input 1 :
1 2 3 N N 4 6 N 5 N N 7 N

Sample Output 1 :
[ [1 2], [1 3 4 5 7],[1 3 6] ]

"""

"""
Time Complexity:    
Space Complexity: 
"""

"""
definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def Paths(self, root : Optional['Node']) -> List[List[int]]:
        # code here
        res = []
        
        def in_order_path(cur_node, path):
            if not cur_node:
                return
        
            
            in_order_path(cur_node.left, path+[cur_node.data])
            
            if not cur_node.left and not cur_node.right:
                res.append(path+[cur_node.data])
                
            in_order_path(cur_node.right, path + [cur_node.data])
        
        in_order_path(root, [])
        return res  
            