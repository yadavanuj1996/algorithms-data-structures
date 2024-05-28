Sure, let's expand on each step of the boundary traversal algorithm to provide a more detailed explanation.

### Detailed Steps

1. **Initialize Result**:
   - Start with the root node's data.
   - If the root node is `None`, return an empty list as the boundary traversal.

2. **Left Boundary**:
   - Traverse the left boundary excluding the leaf nodes.
   - Start from the left child of the root.
   - Continue moving to the left child if it exists; otherwise, move to the right child.
   - Stop the traversal when reaching a leaf node (a node with no left or right children).
   - Add the node's data to the result list.

3. **Leaf Nodes**:
   - Use an inorder traversal to collect all the leaf nodes (nodes with no left or right children).
   - This traversal ensures the left-to-right order of leaf nodes.
   - Recursively visit the left subtree, then the current node, and finally the right subtree.
   - If a node is a leaf node, add its data to the result list.

4. **Right Boundary**:
   - Traverse the right boundary excluding the leaf nodes.
   - Start from the right child of the root.
   - Use a stack to collect nodes' data to reverse the order later.
   - Continue moving to the right child if it exists; otherwise, move to the left child.
   - Stop the traversal when reaching a leaf node.
   - Pop nodes from the stack and add their data to the result list to ensure the order is from bottom to top.

5. **Combine Results**:
   - Combine the left boundary nodes, leaf nodes, and reversed right boundary nodes to form the final boundary traversal list.

### Example Code with Detailed Comments

```python
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def traverseBoundary(root):
    if not root:
        return []

    res = [root.data]
    
    # Helper function to get the left boundary
    def get_left_boundary():
        cur_node = root.left
        while cur_node:
            # Add to result if it's not a leaf node
            if cur_node.left or cur_node.right:
                res.append(cur_node.data)
            # Move to the next left boundary node
            cur_node = cur_node.left if cur_node.left else cur_node.right

    # Helper function to get leaf nodes using inorder traversal
    def leaf_node_in_order(cur_node, leaf_nodes=[]):
        if not cur_node:
            return
        
        # Traverse the left subtree
        leaf_node_in_order(cur_node.left, leaf_nodes)
        
        # Add leaf nodes to the list
        if not cur_node.left and not cur_node.right:
            leaf_nodes.append(cur_node.data)
        
        # Traverse the right subtree
        leaf_node_in_order(cur_node.right, leaf_nodes)
        
        return leaf_nodes

    # Helper function to get the right boundary in reverse order
    def get_right_boundary():
        cur_node = root.right
        stack = []
        while cur_node:
            # Add to stack if it's not a leaf node
            if cur_node.left or cur_node.right:
                stack.append(cur_node.data)
            # Move to the next right boundary node
            cur_node = cur_node.right if cur_node.right else cur_node.left
        
        # Add right boundary nodes to result in reverse order
        while stack:
            res.append(stack.pop())

    # Get left boundary excluding the leaf nodes
    get_left_boundary()
    
    # Get leaf nodes from left to right
    res += leaf_node_in_order(root, [])
    
    # Get right boundary excluding the leaf nodes
    get_right_boundary()
    
    return res

# Example usage:
# Construct a binary tree
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6
#      / \
#     7   8
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right.right = TreeNode(6)

print(traverseBoundary(root))  # Output: [1, 2, 4, 7, 8, 6, 3]
```

### Explanation of the Example

In this example:
- **Left Boundary**: Start from node 2, then node 4.
- **Leaf Nodes**: Nodes 4, 7, 8, and 6.
- **Right Boundary**: Start from node 3, then node 6 (reversed order).

The boundary traversal results in `[1, 2, 4, 7, 8, 6, 3]`, covering the left boundary, all leaf nodes, and the right boundary in the required order.