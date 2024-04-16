### Algorithm Summary:
1. **Initialization**:
   - Initialize the number of nodes in the graph (V).
   - Initialize an empty list to store the result (`result`).
   - Create an empty reverse graph with V nodes (`reverse_graph`) and initialize an in-degree array with zeros (`in_degree`) to represent the in-degree of each node.
   - Initialize an empty queue (`queue`).

2. **Reverse Graph Creation**:
   - Create the reverse graph by iterating over each node in the original graph.
     - Calculate the out-degree (number of outgoing edges) of each node and update the in-degree array accordingly.
     - Build the reverse graph by adding the current node to the adjacency list of its adjacent nodes in the reverse direction.

3. **Identify Nodes with Zero In-Degree**:
   - Identify nodes with zero in-degree and add them to the queue.

4. **Topological Sorting using BFS**:
   - Perform topological sorting using BFS:
     - While the queue is not empty:
       - Remove a node from the queue (`cur_node`).
       - Append `cur_node` to the result list.
       - Iterate over each adjacent node of `cur_node` in the reverse graph.
         - Decrement the in-degree of the adjacent node.
         - If the in-degree of the adjacent node becomes zero, add it to the queue.

5. **Sort the Result**:
   - Sort the result list in ascending order.

6. **Return**:
   - Return the sorted result list.
