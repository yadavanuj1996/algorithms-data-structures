### Algorithm Steps:

1. **Initialization of Data Structures**:
   - Initialize two arrays, `rank` and `parent`, to keep track of the rank and parent of each node in the grid. These arrays are used in the union-find data structure.
   
2. **Definition of Helper Functions**:
   - `get_ultimate_parent(node)`: This function finds the ultimate parent of a node using path compression. It recursively traverses the parent pointers until it reaches the ultimate parent, updating the parent pointers along the way to optimize future lookups.
   - `union_by_rank(u, v)`: This function performs the union by rank operation to merge two sets of nodes. It compares the ranks of the ultimate parents of the two nodes (`u` and `v`) and performs the appropriate union operation.
   - `union_with_neighbour_node(cur_node, r, c, no_of_islands)`: This function finds neighboring nodes of a given node and performs union operations if they are part of different islands. It iterates through adjacent positions (top, right, bottom, left) relative to the current node, checks if the neighboring nodes are valid and belong to different islands, merges them if necessary, and reduces the count of islands.

3. **Initialization of Variables and Data Structures**:
   - Initialize `no_of_islands` to keep track of the number of islands found so far.
   - Initialize `node_set` to keep track of visited nodes.
   - Initialize `adj_matrix` to represent the grid, where each cell contains either 0 (water) or 1 (land).

4. **Iterating Through Queries**:
   - For each query (coordinate pair), update the adjacency matrix with the given queries, marking land cells with 1.
   - Increment `no_of_islands` to account for the newly discovered island.
   - Find the current node (`cur_node`) corresponding to the query and add it to `node_set`.
   - Update `no_of_islands` by calling `union_with_neighbour_node` to merge islands with neighboring nodes, if applicable.
   - Append the updated `no_of_islands` to the result list.

5. **Return Result**:
   - After processing all queries, return the list containing the updated count of islands after each query.

### Summary:
This algorithm efficiently finds the number of islands in the grid by employing the union-find data structure and path compression technique. It iterates through the grid, updates the count of islands, merges islands when necessary, and reduces the count of islands if they are merged during the process. The use of helper functions and appropriate data structures enhances the readability and efficiency of the algorithm.
