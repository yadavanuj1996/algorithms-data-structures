## Approach 1:
![IMG_8281](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/591fb0cb-ca21-4c78-b611-93dc6826bdd4)


## Approach 2:
![IMG_8280](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/ec5d3b9b-206d-41e8-8917-223db0de281f)
![IMG_8279](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/e2ec2e4a-1436-4902-992b-d896a9ab534f)

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
