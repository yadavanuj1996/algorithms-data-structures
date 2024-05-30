![IMG_9450](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/7f19729d-d4f6-4111-a427-48c2a6a6d300)
## Vertical Order Traversal of a Binary Tree

This algorithm performs a vertical order traversal of a binary tree. The nodes are grouped and displayed based on their horizontal distance from the root. Nodes at the same horizontal distance are displayed from top to bottom, and if two nodes share the same position, they are sorted by their values.

### Algorithm Summary

1. **Initialization:**
   - Create an empty result list `res` to store the final output.
   - Use a dictionary `res_dict` to map vertical levels to lists of node values.
   - Use a queue initialized with the root node and its vertical level (0) to perform breadth-first search (BFS).

2. **Breadth-First Search (BFS):**
   - While the queue is not empty:
     - Get the current size of the queue to process all nodes at the current level.
     - Initialize `row_dict` to hold node values for the current level.

     - For each node at the current level:
       - Dequeue the node and its vertical level.
       - Append the node's value to `row_dict` for its vertical level.
       - Enqueue the left child with a vertical level one less than the current node.
       - Enqueue the right child with a vertical level one more than the current node.

   - After processing all nodes at the current level:
     - For each vertical level in `row_dict`, sort the values (if there are multiple values) and append them to `res_dict`.

3. **Result Compilation:**
   - Sort the keys of `res_dict` (i.e., the vertical levels).
   - Append the sorted lists of node values from `res_dict` to `res`.

4. **Return the result list `res`.

### Time Complexity

- **Traversal of the Tree:** The BFS traversal visits each node once, leading to a time complexity of \(O(n)\), where \(n\) is the number of nodes.
- **Sorting Nodes at Each Level:** The node values at each vertical level are sorted. In the worst case, this sorting step has a time complexity of \(O(n \log n)\).
- **Sorting Keys for Final Output:** Sorting the vertical levels has a time complexity of \(O(m \log m)\), where \(m\) is the number of unique vertical levels. Since \(m \leq n\), this is \(O(n \log n)\).

Combining these, the overall time complexity is \(O(n \log n)\).

### Space Complexity

- **Queue:** The BFS queue can hold up to \(O(n)\) nodes in the worst case.
- **Dictionaries:** Both `row_dict` and `res_dict` store node values and can collectively hold up to \(O(n)\) values.
- **Result List:** The result list `res` stores all node values, leading to \(O(n)\) space.

The total space complexity is \(O(n)\).

---

This summary explains the algorithm in a human-readable format suitable for a README file, and includes a detailed analysis of time and space complexity.
