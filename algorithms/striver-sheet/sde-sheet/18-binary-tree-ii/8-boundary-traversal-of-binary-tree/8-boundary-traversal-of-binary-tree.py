"""
Boundary Traversal of Binary Tree

Problem Link:
https://www.naukri.com/code360/problems/boundary-traversal-of-binary-tree_790725

Statement
You are given a binary tree having 'n' nodes.
The boundary nodes of a binary tree include the nodes from the left and right boundaries and the leaf 
nodes, each node considered once.

Figure out the boundary nodes of this binary tree in an Anti-Clockwise direction starting from the 
root node.

Constraints:
- 1 <= n <= 10000
- Time Limit: 1 sec


Test Case:
Sample Input 1:
10 5 20 3 8 18 25 -1 -1 7 -1 -1 -1 -1 -1 -1 -1

Sample Output 1:
10 5 3 7 18 25 20

"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
"""
# Breaking the problem in 3 parts
1. Print all left boundary nodes
2. Print all leaf nodes
3. Print all right boundary nodes in reverse (use stack)
"""
def traverseBoundary(root):
    # Write your code here.
    res = [root.data]
    
    # left boundary
    def get_left_boundary():
        cur_node = root.left

        while cur_node and (cur_node.left or cur_node.right):
            res.append(cur_node.data)
            cur_node = cur_node.left if cur_node.left else cur_node.right

    # leaf nodes using inorder traversal this will make sure the left to right
    # order of leaf nodes will be maintained even if leaf nodes are on different level
    def leaf_node_in_order(cur_node, leaf_nodes=[]):
        if not cur_node:
            return
        
        leaf_node_in_order(cur_node.left)
        if not cur_node.left and not cur_node.right:
            leaf_nodes.append(cur_node.data)
        leaf_node_in_order(cur_node.right)
    
        return leaf_nodes
        
        
    # right boundary reverse order
    def get_right_boundary():
        cur_node = root.right
        stack = []

        while cur_node and (cur_node.left or cur_node.right):
            stack.append(cur_node.data)
            cur_node = cur_node.right if cur_node.right else cur_node.left
        
        # emptying stack and adding to result, this will reverse the node order
        while stack:
            res.append(stack.pop())


    # left boundary
    get_left_boundary()
    # lead nodes from left to right
    res += leaf_node_in_order(root)
    # right boundary
    get_right_boundary()

    
    return res
