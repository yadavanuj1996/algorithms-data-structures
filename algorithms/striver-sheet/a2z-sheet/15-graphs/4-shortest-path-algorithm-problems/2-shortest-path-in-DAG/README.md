## Approach 2: TOPO sort with DFS combination
![IMG_8349](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/0bf01429-a7a4-4113-aae6-d3fcf5df09e5)

This algorithm is aimed at finding the shortest paths in a Directed Acyclic Graph (DAG). Here's a summary:

1. **Topological Sorting**:
   - Utilizes a topological sorting approach using a stack. The function `get_topo_sort_order` takes the number of nodes `n` and the adjacency list `adj_list` as input.
   - It initializes an empty stack and a visited array to mark nodes as visited during traversal.
   - Defines a recursive `topo_sort` function that marks nodes as visited and recursively explores their adjacent nodes, pushing them onto the stack.
   - Starts the topological sort from node 0 and returns the topologically sorted stack.

2. **Shortest Path Calculation**:
   - The `shortestPathInDAG` function takes the number of nodes `n`, the number of edges `m`, and the list of edges `edges` as input.
   - Initializes an adjacency list `adj_list` and a distance array `dist` with -1 for each node.
   - Populates the adjacency list with the given edges.
   - Performs topological sorting using the `get_topo_sort_order` function and retrieves the topologically sorted stack.
   - Sets the distance of the source node (top element of the stack) to 0.
   - While the stack is not empty, it pops a node `cur_node` from the stack and iterates through its adjacent nodes.
   - Updates the distance for each adjacent node if the new path is shorter.
   - Returns the array containing the shortest distances from the source node to all other nodes in the graph.

This algorithm effectively leverages topological sorting and dynamic programming to compute shortest paths in a DAG efficiently.

## Approach 1: Normal DFS
![IMG_8348](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/d8c806ef-471c-4464-b8fc-40db0b024816)

# Algorithm Summary: Depth-First Search for Shortest Distances in a Directed Acyclic Graph (DAG)

This algorithm implements a Depth-First Search (DFS) on a Directed Acyclic Graph (DAG) to find the shortest path distances from a given source node to all other nodes in the graph. Here's a summary of the algorithm:

1. **Initialization**: Initialize an empty adjacency list to represent the graph and an array to store the shortest distances from the source node to each node in the graph.

2. **Populating Adjacency List**: Populate the adjacency list with the given edges, where each edge consists of a source node, a destination node, and a weight.

3. **DFS Function**: Define a recursive depth-first search function (`dfs`) that takes the current node and the distance from the source node to the current node.

4. **DFS Traversal**:
   - If the distance to the current node is not calculated yet or the newly calculated distance is shorter than the previous one, update the distance.
   - Recursively call the DFS function for each adjacent node of the current node, updating the distance accordingly by adding the weight of the edge.

5. **Starting DFS**: Start the DFS from the source node (node 0) with an initial distance of 0.

6. **Result**: Return the array containing the shortest distances from the source node to all other nodes in the graph.

This algorithm traverses the entire graph using DFS, updating the shortest distance to each node as it explores the graph. Since it's a DAG, there are no cycles, ensuring that the algorithm terminates successfully.

