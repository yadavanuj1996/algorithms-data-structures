
![IMG_7981](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/938f548a-2502-4a73-81d5-08f9c8625451)

## Algorithm Summary

1. **Coloring Nodes for Bipartite Check**:
   - The algorithm initializes two lists: `visited` to keep track of visited nodes and `is_colored` to assign colors (True or False) to each node. Both lists are initially filled with default values.
   - It defines a recursive function `color_node(cur_node, color=True)` to color nodes and their adjacent nodes:
     - The function checks if the current node has already been visited. If it has, it checks if the current color assignment matches the previous color assignment. If not, it returns False, indicating a conflict.
     - If the current node hasn't been visited, it marks it as visited and assigns it the specified color.
     - Then, it recursively colors its adjacent nodes with the opposite color, ensuring bipartite property.
     - The function returns True if coloring is successful without conflicts.
   - This coloring process effectively determines whether the graph is bipartite or not.

2. **Iterating and Coloring Nodes**:
   - The algorithm iterates through each node in the graph.
   - For each unvisited node, it calls the `color_node` function.
   - If `color_node` returns False for any node, indicating that the graph is not bipartite, the algorithm immediately returns False.

3. **Final Result**:
   - If the iteration completes without finding any conflicts, the algorithm returns True, indicating that the graph is bipartite.

