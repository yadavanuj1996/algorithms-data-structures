This algorithm is an implementation of Dijkstra's algorithm for finding the shortest paths from a single source node to all other nodes in a weighted graph. Here's a detailed explanation:

1. **Initialization**:
   - Initialize an adjacency list `adj_list` to represent the graph, where each node contains a list of its neighboring nodes along with the corresponding edge weights.
   - Initialize an array `distances` to store the shortest distance from the source node to each node in the graph. Initialize all distances to infinity except for the distance from the source node to itself, which is set to 0.

2. **Populating the Graph**:
   - Populate the adjacency list `adj_list` with the provided edge information. Each edge is represented as a tuple `(source, destination, weight)`.

3. **Initializing Priority Queue**:
   - Initialize a priority queue (min-heap) `priority_queue` to store nodes along with their current shortest distance from the source node. Push the source node `source_node` with distance 0 into the priority queue.
   - Update the distance of the source node `source_node` to 0 in the `distances` array.

4. **Dijkstra's Algorithm Loop**:
   - While the priority queue is not empty:
     - Pop the node with the smallest distance from the priority queue.
     - For each neighboring node of the current node:
       - Update its distance if the new distance through the current node is shorter than the previously recorded distance.
       - Push the updated distance and node into the priority queue.

5. **Finding Maximum Distance**:
   - After the loop, find the maximum distance recorded in the `distances` array by iterating through all nodes.
   - Update `max_distance` with the maximum distance found.

6. **Returning Result**:
   - Return `max_distance` if it is not infinite, indicating a reachable node from the source node `source_node`. Otherwise, return -1, indicating that the node is unreachable.

This algorithm efficiently computes the maximum shortest distance from the source node `source_node` to any other node in the graph.
