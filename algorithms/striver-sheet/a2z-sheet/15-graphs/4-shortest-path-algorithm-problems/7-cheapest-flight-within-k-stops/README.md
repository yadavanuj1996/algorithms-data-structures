1. **Initialize Graph Representation**:
   - Create an empty adjacency list `adj_list` to represent the graph.
   - Initialize an array `dist` to store the shortest distance from the source node to each node. Set all distances to infinity initially.

2. **Populate Adjacency List**:
   - Iterate through the `flights` list, which contains tuples `(source, destination, weight)`.
   - For each flight, add the destination node and its weight to the adjacency list under the source node.

3. **Initialize BFS Queue**:
   - Create an empty queue `queue` to perform breadth-first search traversal.
   - Enqueue a tuple `(0, src, 0)` representing the number of stops (initially 0), the source node, and the distance to the source node (initially 0).

4. **Breadth-first Search**:
   - While the queue is not empty:
     - Dequeue a tuple `(no_of_stops, cur_node, dist_to_node)` from the queue.
     - If `no_of_stops` exceeds the maximum allowed stops `k`, terminate the search.
     - Iterate through the neighbors of `cur_node` using the adjacency list.
     - Update the distance to each neighbor if the distance via `cur_node` is shorter than its current distance.
     - Enqueue the neighbor if its distance was updated.

5. **Result**:
   - Return the shortest distance to the destination node (`dst`) from the source node (`src`) stored in `dist`.
   - If the destination is unreachable, return -1.
