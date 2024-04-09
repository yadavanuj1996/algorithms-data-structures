![IMG_7945](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/11416505-7f24-4bd8-8819-588ef1f7d566)

1. **Finding Boundary 'O' Regions**:
   - A nested function `mark_boundary_o(row, col)` recursively marks 'O' regions connected to the boundary.
   - It marks the boundary 'O' regions as `None` to differentiate them from captured regions and prevent reprocessing.
   - Traverses in four directions (top, right, bottom, left) from the current position and marks connected 'O' regions recursively.

2. **Processing Boundary**:
   - Iterates over the first and last rows, as well as the first and last columns.
   - For each 'O' cell encountered, it calls `mark_boundary_o` to mark connected 'O' regions.

3. **Processing Remaining Cells**:
   - After marking boundary 'O' regions, iterates over all cells in the board.
   - Replaces 'O' cells (that were not marked as boundary) with 'X' to capture surrounded regions.
   - Replaces `None` cells with 'O' to restore unaffected regions.

Overall, this algorithm effectively captures regions surrounded by 'X' on the board by marking boundary 'O' regions and then updating the board accordingly.
