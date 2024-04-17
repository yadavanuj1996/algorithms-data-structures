![IMG_8376](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/3e15aef9-1910-4184-a03c-d9af3a96f340)

This Python solution implements a BFS (Breadth-First Search) algorithm to find the shortest path in a binary grid. Here's a summary of the algorithm:

1. The algorithm starts with a queue containing the source node `(0, 0, 0)`, where the first two values represent the row and column indices, and the third value represents the distance from the source node.
  
2. It initializes a `visited` matrix to keep track of visited cells and a `queue` for BFS traversal.

3. The algorithm dequeues nodes from the queue until it's empty.

4. For each dequeued node, it checks if it's valid (within grid bounds, not blocked by a wall, and not visited). If not, it skips to the next iteration.

5. If the dequeued node is the destination node `(no_of_rows-1, no_of_cols-1)`, the algorithm returns the distance + 1 because the number of cells in the path equals the number of edges plus 1.

6. If the dequeued node is not the destination, the algorithm enqueues its adjacent cells (up, down, left, right, and diagonals) with distances incremented by 1.

7. If no path is found, the algorithm returns -1.

This algorithm efficiently explores all possible paths from the source node `(0, 0)` to the destination node `(no_of_rows-1, no_of_cols-1)` using BFS, ensuring that the shortest path is found.
