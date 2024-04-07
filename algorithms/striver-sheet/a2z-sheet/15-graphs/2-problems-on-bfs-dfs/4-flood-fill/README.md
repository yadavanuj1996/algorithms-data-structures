# Algorithm Summary

1. **Initialization:**
    - Initialize the total number of rows (`total_rows`) and columns (`total_cols`) in the image matrix.

2. **Flood Fill Function (`fill_color`):**
    - Define a nested function `fill_color` to perform flood fill using Depth-First Search (DFS).
        - Perform boundary checks to ensure valid pixel positions within the image matrix.
        - Check if the current pixel's color is not equal to the previous color or it's already the new color, in which case return.
        - Update the current pixel's color to the new color.
        - Recursively call `fill_color` for the neighboring pixels (top, right, bottom, left) of the current pixel.

3. **Flood Fill Invocation:**
    - Call `fill_color` with the starting row (`sr`), starting column (`sc`), and `None` as the previous color to initiate the flood fill.

4. **Return:**
    - Return the modified image matrix.

5. **Complexity Analysis:**
    - *Time Complexity*: O(4 * N * M), where N and M are the number of rows and columns in the image matrix, respectively. In the worst case, the `fill_color` function will be called 4 times for each node.
    - *Space Complexity*: O(N * M), due to the recursion stack space used by the DFS algorithm.
