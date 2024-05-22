### Algorithm Summary

#### Three Conditions to Check if a Binary Tree (BT) is Height Balanced:
1. The difference between the heights of the left and right subtrees for any node is not more than one.
2. The left subtree is balanced.
3. The right subtree is balanced.

#### Explanation:
- **Base Case**: If the current node is `None`, it returns a height of 0.
- **Recursive Case**:
  - It recursively computes the heights of the left and right subtrees.
  - If any subtree is found to be unbalanced (returns -1), it propagates -1 upwards.
  - It checks the absolute difference in heights between the left and right subtrees. If this difference exceeds 1, it marks the current subtree as unbalanced by returning -1.
  - If balanced, it returns the height of the current node as `1 + max(left_height, right_height)`.
- **Final Check**: The `isBalanced` function returns `True` if the whole tree is balanced (i.e., `get_height` does not return -1), otherwise it returns `False`.

### Complexity Analysis:

- **Time Complexity:** \( O(n) \)
  - The tree is traversed once to calculate heights and diameters.
  
- **Space Complexity:** \( O(n) \)
  - In the worst case, the recursive call stack will store all nodes (in the case of a skewed tree).

This algorithm ensures an efficient computation of the tree's diameter by leveraging a single post-order traversal.