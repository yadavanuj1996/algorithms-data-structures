## Overview
The `get_lca` function is designed to find the lowest common ancestor (LCA) of two nodes in a binary
tree. The LCA of two nodes `p` and `q` is defined as the deepest node that has both `p` and `q` as 
descendants (where a node can be a descendant of itself).

## Algorithm
1. **Base Case**: If the current node is `None` or matches either `p` or `q`, return the current node.
2. **Recursive Search**: Recursively search the left and right subtrees for `p` and `q`.
3. **Determine LCA**:
   - If both left and right recursive calls return non-`None` values, the current node is the LCA.
   - If only one of the left or right recursive calls returns a non-`None` value, return the non-`None` value.
   - If both recursive calls return `None`, return `None`.

## Complexity Analysis
- **Time Complexity**: `O(N)`
  - The function visits each node of the tree once, where `N` is the number of nodes in the tree.
- **Space Complexity**: `O(H)`
  - The function uses a stack for recursion that can go as deep as the height `H` of the tree. In the worst case, the height of the tree can be `N` (in case of a skewed tree).

