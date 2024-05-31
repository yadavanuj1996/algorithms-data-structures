# Binary Tree Sum Property Check

## Overview
This repository contains a solution to check whether all nodes in a binary tree satisfy the property that each node's value is equal to the sum of its child nodes' values.

## Node Class
```python
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
```


This method checks if every node in the binary tree has a value equal to the sum of its left and right child nodes' values. If a node is a leaf node (i.e., it has no children), it trivially satisfies this property.

#### Algorithm
1. **Base Case**: If the current node is `None`, return `1` (true).
2. **Calculate Child Sum**: Compute the sum of the values of the left and right children of the current node. If a child is `None`, its value is considered `0`.
3. **Check Node Value**: Compare the current node's value with the calculated child sum. If they are not equal and the child sum is not `0`, return `0` (false).
4. **Recursive Check**: Recursively check the left and right subtrees to ensure they also satisfy the sum property.
5. **Return Result**: Return `1` (true) if the entire tree satisfies the sum property, otherwise return `0` (false).

### Time Complexity
The time complexity of the `isSumProperty` method is \(O(N)\), where \(N\) is the number of nodes in the binary tree. This is because each node is visited once during the traversal.

### Space Complexity
The space complexity of the `isSumProperty` method is \(O(H)\), where \(H\) is the height of the binary tree. This space is used by the call stack during the recursive traversal. In the worst case (for a skewed tree), this can be \(O(N)\).

## Example
```python
# Constructing a sample tree
#        10
#       /  \
#      4    6
#     / \  / \
#    2  2 3   3

root = Node(10)
root.left = Node(4)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(2)
root.right.left = Node(3)
root.right.right = Node(3)

solution = Solution()
print(solution.isSumProperty(root))  # Output: 1 (True)
```

---

This summary provides an overview of the implementation, the algorithm used, and the complexities associated with the method.