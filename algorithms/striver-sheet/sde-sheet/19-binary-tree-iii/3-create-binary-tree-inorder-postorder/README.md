### Algorithm Summary

The algorithm reconstructs a binary tree from its inorder and postorder traversal arrays. It follows these steps:

1. **Base Case**: If the `inorder` array is empty, return `None`.
2. **Identify Root**: The last element in the `postorder` array is the root of the current subtree.
3. **Find Root Index in Inorder**: Determine the index of this root value in the `inorder` array.
4. **Split Arrays for Subtrees**:
    - **Left Subtree**: Elements before the root index in `inorder` and the corresponding elements in `postorder`.
    - **Right Subtree**: Elements after the root index in `inorder` and the remaining elements in `postorder`.
5. **Recursive Construction**: Recursively apply the same logic to construct the left and right subtrees.
6. **Link Subtrees**: Attach the constructed left and right subtrees to the root node.

### Time Complexity (TC) and Space Complexity (SC)

- **Time Complexity**: O(n^2)
  - Finding the index of the root in the `inorder` array takes O(n) time.
  - This index search happens for each node, leading to an O(n^2) complexity.

- **Space Complexity**: O(n)
  - The space complexity is primarily due to the recursion stack, which in the worst case (unbalanced tree) can go up to O(n).

### Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def build_tree(in_order: List[int], post_order: List[int]) -> Optional[TreeNode]:
            if len(in_order) == 0:
                return None
            
            cur_root = TreeNode(val=post_order[-1])
            cur_root_in_order_index = in_order.index(cur_root.val)
            
            # Left child creation
            left_in_order = in_order[0:cur_root_in_order_index]
            left_post_order = post_order[0:cur_root_in_order_index]

            # Call recursive function for left child
            cur_root.left = build_tree(left_in_order, left_post_order)
            
            # Right child creation
            right_in_order = in_order[cur_root_in_order_index + 1:]
            right_post_order = post_order[cur_root_in_order_index:-1]
            
            # Call recursive function for right child
            cur_root.right = build_tree(right_in_order, right_post_order)

            return cur_root

        return build_tree(inorder, postorder)
```

### Example Explanation

Consider `inorder = [9, 3, 15, 20, 7]` and `postorder = [9, 15, 7, 20, 3]`.

1. **Initial Call**:
   - `inorder = [9, 3, 15, 20, 7]`
   - `postorder = [9, 15, 7, 20, 3]`
   - Root is `3`.

2. **Split Arrays**:
   - **Left Subtree**:
     - `inorder = [9]`
     - `postorder = [9]`
   - **Right Subtree**:
     - `inorder = [15, 20, 7]`
     - `postorder = [15, 7, 20]`

3. **Recursive Calls**:
   - **Left Subtree**:
     - Root is `9`.
     - No further splits needed.
   - **Right Subtree**:
     - Root is `20`.
     - **Left Subtree**:
       - `inorder = [15]`
       - `postorder = [15]`
     - **Right Subtree**:
       - `inorder = [7]`
       - `postorder = [7]`

4. **Constructed Tree**:
   - The tree is reconstructed by linking all nodes appropriately based on the recursion and splits:
     ```
           3
         /   \
        9     20
             /  \
            15   7
     ```

This process is repeated until all nodes are placed in their correct positions in the tree.