"""
Tree Traversals

Problem Link:
https://www.naukri.com/code360/problems/981269

Statement:
You have been given a Binary Tree of 'N' nodes, where the nodes have integer values.
Your task is to return the ln-Order, Pre-Order, and Post-Order traversals of the given binary
tree.

Constraints:
- 1 ≤ N ≤ 10^5
- 1 ≤ Node Data ≤ 10^5

Test Case:
Sample Input 1 :
1 2 3 -1 -1 -1  6 -1 -1

Sample Output 1 :
2 1 3 6  # in order
1 2 3 6  # pre order
2 6 3 1  # post order

"""

"""
Time Complexity: O(N), single_traversal fn is called once for each node 
Space Complexity: O(N) , in details O(3N) + O(H) .

The lists pre_order, in_order, and post_order each store one element per node thus O(3N)
O(H) for recursion stack where h is height of tree best case O(log N) worst case O(N) for 
skewed tree we will take O(N) from it as well.
"""

from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # Write your code here.
    pre_order = []
    in_order = []
    post_order = []

    def single_traversal(cur_node):
        if not cur_node:
            return 
        
        pre_order.append(cur_node.data)
        single_traversal(cur_node.left)
        in_order.append(cur_node.data)
        single_traversal(cur_node.right)
        post_order.append(cur_node.data)

    single_traversal(root)
    return [in_order, pre_order,post_order]

