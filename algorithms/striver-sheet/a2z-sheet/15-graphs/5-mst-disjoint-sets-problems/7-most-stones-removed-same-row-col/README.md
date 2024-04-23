![IMG_8706](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/1ad8b042-1cc2-42dc-a048-9e0ca2e6e2c2)
![IMG_8707](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/372630d4-a8a3-4edc-8d1f-d029c80a0dc6)
![IMG_8708](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/212346ff-fb3b-440c-96ff-529003cec334)


1. **Initialization**:
   - Initialize `max_row` and `max_col` to 0. These variables will keep track of the maximum row and column indices of the stones.
   - Initialize `stone_count` to 0, representing the number of stones.

2. **Iterate through Stones**:
   - Iterate through each stone in the input list `stones`.
   - Update `max_row` and `max_col` by comparing with the current stone's row and column indices.

3. **Calculate Total Nodes**:
   - Calculate the total number of nodes (`total_nodes`) considering both rows and columns.
   - `total_nodes = max_row + 1 + max_col + 1`, where `max_row + 1` accounts for rows and `max_col + 1` accounts for columns.

4. **Disjoint Set Union (DSU)**:
   - Initialize two arrays: `rank` and `parent`.
   - `rank` will store the rank of each node, and `parent` will store the parent node of each node.
   - Initially, each node is its own parent, and the rank of each node is 0.

5. **Find Ultimate Parent**:
   - Define a function `get_ultimate_parent(node)` to find the ultimate parent of a node in the DSU tree.
   - This function recursively finds the ultimate parent of a node and compresses the path by updating the parent of intermediate nodes.

6. **Union by Rank**:
   - Define a function `union_by_rank(u, v)` to perform union by rank operation.
   - This function joins two nodes (`u` and `v`) by their ultimate parents while considering the rank to maintain a balanced tree.
   - If the ranks of the ultimate parents are equal, one tree's rank is incremented.

7. **Process Stones**:
   - Iterate through each stone in the input list `stones`.
   - Convert the stone's column index to a unique identifier by adding `max_row + 1` to it.
   - Perform `union_by_rank()` on the row and column nodes of the stone to merge them into the same set.

8. **Count Components**:
   - Create a set `node_set` to store unique nodes that have stones on them.
   - Iterate through `node_set` and count nodes whose ultimate parent is itself. Each such node represents a connected component.

9. **Calculate Remaining Stones**:
   - Subtract the number of connected components from the total number of stones to get the maximum number of stones that can remain after removal.
   - `remaining_stones = stone_count - number_of_components`.

This detailed summary provides a comprehensive explanation of the algorithm, including variable names and step-by-step operations.
