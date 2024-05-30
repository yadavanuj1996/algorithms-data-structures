"""
Mirror Tree

Problem Link:
https://www.geeksforgeeks.org/problems/mirror-tree/1

Statement
Given a Binary Tree, convert it into its mirror.

Constraints:
- 1 ≤ Number of nodes ≤ 10^5
- 1 ≤ Data of a node ≤ 10^5


Test Case:
Sample Input 1:
1 2 3

Sample Output 1:
3 1 2 (in order)

Sample Input 2:
1 2 3 4 5 6 7

Sample Output 2:
7 3 6 1 5 2 4 (In order)

"""

"""
Time Complexity: O(N) , no of nodes
Space Complexity: O(h), H height of tree worst case O(n) skewed tree
"""

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        
        def post_order_swap(cur_node):
            if not cur_node:
                return 
            
            post_order_swap(cur_node.left)
            post_order_swap(cur_node.right)
            
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
    
        post_order_swap(root)
        
        return root
            
       