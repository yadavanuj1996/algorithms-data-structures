Algorithm Summary:
1. Initialize the number of provinces (`no_of_provinces`) to 0.
2. Initialize a boolean list `is_visited` to keep track of visited nodes. Initially, all nodes are marked as unvisited.
3. Define a depth-first search (DFS) function (`dfs`) to traverse the graph recursively. 
    - When visiting a node, mark it as visited.
    - For each adjacent node that is connected (`isConnected[cur_node][adj_node] == 1`), recursively call the DFS function on it.
4. Iterate through each city node (`cur_city_node`) in the graph.
    - If the city node hasn't been visited, it means it belongs to a new province. Increment `no_of_provinces` and perform DFS from this node to mark all connected nodes.
5. Finally, return the total number of provinces.

