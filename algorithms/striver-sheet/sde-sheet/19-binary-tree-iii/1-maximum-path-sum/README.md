## Maximum Path Sum in Binary Tree

This repository contains the implementation of an algorithm to find the maximum path sum in a binary tree. The maximum path sum is defined as the highest sum of values obtained by traversing any path in the tree. A path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.

### Algorithm

The algorithm follows these steps:

1. **Initialize a variable to store the maximum path sum**: This variable (`max_sum`) is initialized to negative infinity to ensure any path sum found will be larger.
2. **Define a recursive function to calculate the path sum**:
   - If the current node is `None`, return 0 (base case).
   - Calculate the sum of the left and right subtrees recursively.
   - If the sum of the left or right subtree is negative, reset it to 0 to ignore paths that would decrease the overall sum.
   - Update the `max_sum` with the maximum value obtained by considering the current node's value plus the sum of the left and right subtrees.
   - Return the maximum path sum where the current node is the end point, which is the current node's value plus the greater of the sums of the left and right subtrees.
3. **Invoke the recursive function** with the root of the tree.
4. **Return the maximum path sum** found.

### Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float("-inf")]
        
        def path_sum_in_order(cur_node):
            if not cur_node:
                return 0
            
            cur_sum = cur_node.val
            left_sum = path_sum_in_order(cur_node.left)
            right_sum = path_sum_in_order(cur_node.right)
            
            if left_sum < 0:
                left_sum = 0

            if right_sum < 0:
                right_sum = 0

            max_sum[0] = max(max_sum[0], cur_sum + left_sum + right_sum)
            
            return max(cur_sum + left_sum, cur_sum + right_sum)

        path_sum_in_order(root)
        return max_sum[0]
```

### Time Complexity

The time complexity of the algorithm is \(O(N)\), where \(N\) is the number of nodes in the binary tree. This is because each node is visited once during the traversal.

### Space Complexity

The space complexity of the algorithm is \(O(H)\), where \(H\) is the height of the binary tree. This space is used by the recursion stack during the depth-first traversal. In the worst case (a completely unbalanced tree), the height of the tree could be \(N\), leading to a space complexity of \(O(N)\). In the best case (a balanced tree), the height is \(\log N\), leading to a space complexity of \(O(\log N)\).