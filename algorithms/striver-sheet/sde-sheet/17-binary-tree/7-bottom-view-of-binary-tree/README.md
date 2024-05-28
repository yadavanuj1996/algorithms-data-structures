![IMG_9446](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/6e165796-dddd-4398-9ef3-9850795085e9)

## Algorithm Summary: Bottom View of a Binary Tree

### Overview
The algorithm computes the bottom view of a binary tree. The bottom view is the set of nodes visible when the tree is viewed 
from the bottom. Nodes are considered in vertical order, from the leftmost vertical level to the rightmost.

### Steps
1. **Edge Case Handling**: If the root is `None`, return an empty list.
2. **Initialize Data Structures**:
    - Use a deque to perform a level-order traversal (BFS).
    - Use a dictionary to store the bottom-most node at each vertical level.
3. **Level-Order Traversal**:
    - Dequeue the current node and its vertical level.
    - Update the dictionary with the current node's data for its vertical level.
    - Enqueue the left child with a vertical level one less than the current node's.
    - Enqueue the right child with a vertical level one more than the current node's.
4. **Result Compilation**:
    - Sort the result dict
    - Extract the values from the dictionary in order of increasing vertical levels.
    - Return the resulting list of node values.

### Time Complexity
- The time complexity is O(N) + O(K log K), where \(N\) is the number of nodes in the tree & K is the no of vertical lines (worse case it will be N)
  
### Space Complexity
- The space complexity is \(O(N)\) due to the storage required for the queue and dictionary.

### Example Code

```python
from collections import deque

class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def bottomView(self, root):
        if not root:
            return []
        
        # Initialize queue for BFS and dictionary to store bottom view nodes
        queue = deque([(root, 0)])
        res_dict = {}
        
        # Perform level-order traversal
        while queue:
            cur_node, ver_level = queue.popleft()
            
            # Update dictionary with the bottom-most node at each vertical level
            res_dict[ver_level] = cur_node.data
            
            # Enqueue left child with vertical level -1
            if cur_node.left:
                queue.append((cur_node.left, ver_level - 1))
            
            # Enqueue right child with vertical level +1
            if cur_node.right:
                queue.append((cur_node.right, ver_level + 1))
        
        # Extract and return the bottom view in sorted order of vertical levels
        res = []
        for index in sorted(res_dict):
            res.append(res_dict[index])
        
        return res

```
