### Summary

This Python script defines a method `zigzagLevelOrder` that performs a zigzag level order traversal on a binary tree. The traversal alternates the direction of traversal at each level, moving left-to-right on one level and right-to-left on the next.

### Method Explanation

- **Initialization**:
  - If the root is `None`, the function returns `None`.
  - A queue (`deque`) is used to facilitate level order traversal starting with the root node.
  - A boolean flag `is_left_to_right` is initialized to `True` to control the traversal direction.
  - An empty list `res` is initialized to store the results.

- **Traversal**:
  - The outer `while` loop continues until the queue is empty.
  - For each level, determine the number of nodes (`size`) and initialize a list `res_row` to store the current level's values.
  - The inner `for` loop processes each node in the current level:
    - Nodes are popped from the left of the queue.
    - Depending on the direction (`is_left_to_right`), nodes' values are inserted into `res_row` at the appropriate index. (i or size-i-1)
    - If the current node has left or right children, they are appended to the queue for the next level.
  - After processing all nodes at the current level, `res_row` is added to `res`.
  - The direction flag `is_left_to_right` is toggled for the next level.

- **Return**:
  - The function returns the list `res` containing the zigzag level order traversal of the binary tree.

### Time and Space Complexity

- **Time Complexity**: \(O(n)\)
  - Each node is visited exactly once.
  - Operations within the loop are constant time relative to the number of nodes.
  
- **Space Complexity**: \(O(n)\)
  - The space complexity is primarily due to the queue and the result list, which in the worst case, both grow linearly with the number of nodes.

### Code
```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        queue = deque([root])
        is_left_to_right = True
        res = []
    
        while queue:
            size = len(queue)
            res_row = [0] * size
            
            for i in range(size):
                cur_node = queue.popleft()
                
                index = i if is_left_to_right else size - i - 1
                res_row[index] = cur_node.val

                if cur_node.left:
                    queue.append(cur_node.left)
                
                if cur_node.right:
                    queue.append(cur_node.right)

            res.append(res_row)
            is_left_to_right = not is_left_to_right
            
        return res
```

This method provides an efficient way to perform a zigzag level order traversal on a binary tree, leveraging a queue to manage the nodes at each level and a flag to alternate the traversal direction.