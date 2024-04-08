We are using Breadth First Approach (BFS)

We have used BFS because we are finding for min distance and we do not want to go dfs way as it will go in depth
rather than looking for min this will make unnecessary recursion calls and would not solve our purpose

![IMG_7856](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/549b7a9e-5f60-4083-bc14-e16f3b09ac6e)


## Algorithm Summary:
1. Initialize variables:
   - `total_rows` and `total_cols` to store the number of rows and columns in the matrix.
   - `queue` to store the indices of cells to be visited.
   - `is_visited` to keep track of visited cells.
   - `result` to store the distance from each cell to the nearest 0 cell.

2. Iterate through the matrix to find all cells with value 0. For each such cell:
   - Add its indices to the queue.
   - Mark it as visited.

3. Define a helper function `add_adj_element(row, col, steps)` to:
   - Check if the given indices are valid and the cell is not visited.
   - Mark the cell as visited.
   - Add the cell's indices and steps to the queue.

4. While the queue is not empty, pop a cell from the queue and process it:
   - Record the distance from the nearest 0 cell in the `result` matrix.
   - Add adjacent cells to the queue using the `add_adj_element` function with incremented steps.

5. Return the `result` matrix containing distances from each cell to the nearest 0 cell.
