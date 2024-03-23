## Approach and Implementation

**Approach:**

This code utilizes a **Depth-First Search (DFS)** algorithm with **backtracking** to find all possible paths a rat can take through a maze.

**Implementation:**

- The `ratMaze(matrix)` function takes a 2D boolean matrix (`matrix`) representing the maze as input.
- It returns a list of strings (`result`), where each string represents a valid path as a sequence of directions (`U` for Up, `R` for Right, `D` for Down, `L` for Left).
- A helper function `rat_maze(row, col, cur_seq)` recursively explores all four possible directions (Up, Right, Down, Left) from the current position (`row`, `col`).
- It uses a `visited` matrix to track visited cells and avoid revisiting them.
- The function builds the current path sequence (`cur_seq`) by appending directions during exploration.
- Backtracking is applied:
    - If the path reaches the destination (`row == n-1` and `col == n-1`), the path (`cur_seq`) is added to the results list (`result`).
    - Otherwise, the function backtracks after exploring each direction by setting the corresponding cell in `visited` back to `False`.
