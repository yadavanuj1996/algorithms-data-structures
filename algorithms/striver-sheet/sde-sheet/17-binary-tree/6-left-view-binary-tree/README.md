## Algorithm Summary: Left View of a Binary Tree

1. **Initialization**:
   - Create a list `res` to store the left view nodes.

2. **Define a Recursive Function**:
   - Define a recursive helper function `left_view` that takes three parameters: `res`, `cur_node`, and `cur_level`.
     - `res`: The list that stores the left view nodes.
     - `cur_node`: The current node being processed.
     - `cur_level`: The current level in the tree.

3. **Base Case**:
   - If `cur_node` is `None`, return from the function (end the recursion for that path).

4. **Process the Current Node**:
   - If the current level `cur_level` is equal to the length of `res`, it means this is the first time we are visiting a node at this level. Hence, add the node's data to `res`.

5. **Recursive Calls**:
   - First, recursively call `left_view` for the left child of the current node with the next level (`cur_level + 1`).
   - Then, recursively call `left_view` for the right child of the current node with the next level (`cur_level + 1`).

6. **Invoke the Recursive Function**:
   - In the main function `LeftView`, initialize the `res` list and call `left_view` starting from the root node at level 0.

7. **Return the Result**:
   - After completing the recursive traversal, return the list `res` containing the left view nodes.

**Time Complexity**: \(O(n)\) — where \(n\) is the number of nodes in the binary tree. Each node is visited exactly once.

**Space Complexity**: \(O(h)\) — where \(h\) is the height of the tree. This accounts for the recursion stack.
