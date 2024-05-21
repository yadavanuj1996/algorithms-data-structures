## Algorithm Summary: Maximum Depth of a Binary Tree

This algorithm efficiently computes the maximum depth of a binary tree. Here's how it works:

- **Base Case Handling**: When examining a node, if it's `None`, indicating the absence of a subtree, the function returns 0.

- **Recursive Calls**: If the node exists, the function recursively explores its left and right subtrees to determine their heights.

- **Height Calculation**: The height of the current node's subtree is calculated by adding 1 to the maximum height between its left and right subtrees.

- **Return Maximum Depth**: Ultimately, the algorithm returns the height of the entire tree by initiating the recursive process from the root node.

By systematically traversing the binary tree and recursively computing the height of each subtree, the algorithm effectively discerns the maximum depth of the tree.

**Time Complexity**: \(O(n)\) — where \(n\) is the number of nodes in the binary tree. Each node is visited exactly once.

**Space Complexity**: \(O(h)\) — where \(h\) is the height of the tree. This accounts for the recursion stack.