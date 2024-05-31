<img width="851" alt="Screenshot 2024-05-31 at 6 32 13 AM" src="https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/b2e2fe12-f217-44b4-a159-20976fe90c55">

### isSymmetric Algorithm

The `isSymmetric` function checks whether a given binary tree is symmetric around its center. A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree.

#### Algorithm Summary

1. **Initialization:**
   - The function `isSymmetric` is defined within the `Solution` class and takes a `TreeNode` object `root` as its input.
   
2. **Helper Function:**
   - A nested helper function `is_symmetric` is defined to recursively check the symmetry of two nodes (`left_node` and `right_node`).

3. **Base Cases in Helper Function:**
   - If either `left_node` or `right_node` is `None`, the function returns `True` only if both are `None`. If one is `None` and the other is not, it returns `False`.
   - If the values of `left_node` and `right_node` do not match, the function returns `False`.

4. **Recursive Symmetry Check:**
   - The function recursively checks the left subtree of `left_node` against the right subtree of `right_node` and the right subtree of `left_node` against the left subtree of `right_node`.

5. **Initial Call:**
   - The initial call to `is_symmetric` is made with `root.left` and `root.right`.

#### Time Complexity 

- The time complexity of the algorithm is **O(N)**, where N is the number of nodes in the binary tree. This is because each node is visited once in the recursive symmetry check.

#### Space Complexity

- The space complexity of the algorithm is **O(H)**, where H is the height of the tree. This accounts for the space used by the call stack during the recursive calls. In the worst case, this can be O(N) for a completely unbalanced tree, but in the best case of a balanced tree, it would be O(log N).

### Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_symmetric(left_node, right_node):
            # we are checking if nodes or values don't match then return False else keep looking for other nodes
            if not left_node or not right_node:
                return left_node == right_node

            if not left_node.val == right_node.val:
                return False

            return is_symmetric(left_node.left, right_node.right) and is_symmetric(left_node.right, right_node.left)  
        
        return is_symmetric(root.left, root.right)
```

This code efficiently checks whether the given binary tree is symmetric by leveraging a recursive helper function to compare corresponding nodes in the left and right subtrees.
