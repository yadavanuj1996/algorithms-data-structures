"""
Check for Children Sum Property in a Binary Tree

Problem Link:
https://www.geeksforgeeks.org/problems/children-sum-parent/1

Statement
Given a binary tree having n nodes. Check whether all of its nodes have the value equal to the sum of
their child nodes. Return 1 if all the nodes in the tree satisfy the given properties, else it return 0.

For every node, data value must be equal to the sum of data values in left and right children. Consider 
data value as 0 for NULL child.  Also, leaves are considered to follow the property.

Constraints:
- 1 ≤ Number of nodes ≤ 10^5
- 1 ≤ Data of a node ≤ 10^5


Test Case:
Sample Input 1:
35 20 15 15 5 10 5 N N N N 10 N N 5

Sample Output 1:
1
"""

"""
Time Complexity: O(N) , no of nodes
Space Complexity: O(h), H height of tree worst case O(n) skewed tree
"""

"""
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        # code 
        
        def is_sum_property(cur_node):
            if not cur_node:
                return 1
            
            # left sum
            child_sum = cur_node.left.data if cur_node.left else 0
            # right sum
            child_sum += cur_node.right.data if cur_node.right else 0
            
            if not (child_sum == 0 or child_sum == cur_node.data):
                return 0
            
            return is_sum_property(cur_node.left) and is_sum_property(cur_node.right)
            
                
        return is_sum_property(root)   
            
            