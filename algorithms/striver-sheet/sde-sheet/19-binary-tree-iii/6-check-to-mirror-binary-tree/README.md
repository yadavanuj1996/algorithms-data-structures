![IMG_9462](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/7e8543f2-474c-4a66-a851-5ba99f1cd6a3)

## Mirror Binary Tree Algorithm

This Python algorithm converts a binary tree into its mirror tree. The main function `mirror` uses a helper function `post_order_swap` to recursively swap the left and right children of each node in the tree using post-order traversal.

### Algorithm

1. **Function Definition**: The `mirror` function takes the root of the binary tree as an argument.
2. **Helper Function**: Define a nested function `post_order_swap` to perform the node swapping:
   - If the current node (`cur_node`) is `None`, return immediately.
   - Recursively call `post_order_swap` on the left child.
   - Recursively call `post_order_swap` on the right child.
   - Swap the left and right children of the current node.
3. **Invoke Helper**: Call `post_order_swap` starting from the root.
4. **Return Result**: Return the modified tree's root.

### Time Complexity

- **O(n)**: Each node in the tree is visited exactly once, where `n` is the number of nodes in the tree.

### Space Complexity

- **O(h)**: The space complexity is determined by the height of the tree (`h`), due to the recursion stack. In the worst case (a skewed tree), this can be O(n).

### Python Code

```python
class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        
        def post_order_swap(cur_node):
            if not cur_node:
                return 
            
            post_order_swap(cur_node.left)
            post_order_swap(cur_node.right)
            
            cur_node.left, cur_node.right = cur_node.right, cur_node.left
    
        post_order_swap(root)
        
        return root
```
