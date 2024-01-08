
"""
Populating next right pointers in each node

Problem Link:
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

Statement
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


Constraints:
- The number of nodes in the tree is in the range [0, 212 - 1].
- -1000 <= Node.val <= 1000
 
Test Case: ( we have to return root pointer in output)

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
"""


"""
Time Complexity: O(N),      while loop
Space Complexity: O(N),     size of dq
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        dq = deque()
        prev_node_level = 0
        dq.append((root,prev_node_level))
        prev_node = None
        
        while dq:
            element = dq.popleft()
            cur_node = element[0]
            cur_node_level = element[1]

            if cur_node and cur_node.left and cur_node.right:
                dq.append((cur_node.left, cur_node_level+1))
                dq.append((cur_node.right, cur_node_level+1))
            
            if prev_node:
                if cur_node_level > prev_node_level:
                    prev_node.next = None
                else:
                    prev_node.next = cur_node
                
            prev_node = cur_node
            prev_node_level = cur_node_level

        prev_node.next = None

        return root

        