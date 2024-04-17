![IMG_8351](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/93cef1a9-eb00-4fd5-ac0e-dffe6e37e5a9)

This code implements Dijkstra's algorithm to find the shortest paths from a given source node to all other nodes in a graph represented using an adjacency list.
Here's a summary of the algorithm:

1. **Initialize Adjacency List**: Create an empty adjacency list to represent the graph. Iterate through the given edges and add them to the adjacency list. Since the graph is undirected, edges are added for both directions.

2. **Initialize Distance and Priority Queue**: Create an array `dist` to store the shortest distance from the source node to each node. Initialize all distances to infinity except for the distance from the source node, which is set to 0. Create a priority queue to store nodes along with their distances from the source node.

3. **Dijkstra's Algorithm**:
   - While the priority queue is not empty:
     - Pop the node with the minimum distance from the priority queue.
     - Iterate through all adjacent nodes of the current node.
     - For each adjacent node, update its distance if the sum of the current path distance and the distance to the adjacent node is less than the current known distance.
     - If the distance is updated, push the updated distance and node pair into the priority queue.

4. **Return the Shortest Distances**: Once the priority queue becomes empty, return the array `dist` containing the shortest distances from the source node to all other nodes in the graph.

This algorithm ensures that at each step, the node with the shortest known distance from the source is chosen and updated distances are propagated through the graph until the shortest distances to all nodes are found.
