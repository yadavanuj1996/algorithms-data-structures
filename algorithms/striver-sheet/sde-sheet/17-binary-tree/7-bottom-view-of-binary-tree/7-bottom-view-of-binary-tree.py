"""
Bottom View of Binary Tree

Problem Link:
https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

Statement
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

Constraints:
0 <= Number of nodes <= 100
0 <= Data of a node <= 1000


Test Case:

Sample Input 1
1 3 2
Sample Output 1
3 1 2

Sample Input 2
2 7 5 2 6 N 9 N N 5 11 4 N
Sample Output 2
2 5 6 4 9

"""

"""
Time Complexity: O(n), each node will be called upon
Space Complexity: O(n) level order traversal queue size 


"""

from collections import deque

class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []
            
        # cur_node, vertical line
        queue = deque([(root, 0)])
        res_dict = {}
        
        while queue:
            cur_node, ver_level = queue.popleft()
            res_dict[ver_level] = cur_node.data
            
            if cur_node.left:
                queue.append((cur_node.left, ver_level-1))
            
            if cur_node.right:
                queue.append((cur_node.right, ver_level+1))
        
        res = []
        for index in sorted(res_dict):
            res.append(res_dict[index])
    
        return res
            
            
        