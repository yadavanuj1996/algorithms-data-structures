### 1. Define a Recursive Function `find_word(row, col, cur_word_ind)`:
   - **Parameters**:
     - `row`: The current row index being explored.
     - `col`: The current column index being explored.
     - `cur_word_ind`: The index of the current character being matched in the word.
   - **Base Cases**:
     - If `cur_word_ind` equals `word_len`, it means the entire word has been found, so return `True`.
     - If the current cell `(row, col)` is out of bounds (i.e., either the row or column index is less than 0 or greater than or equal to `row_max` or `col_max` respectively), return `False`.
     - If the current cell has already been visited (`visited[row][col]` is `True`) or does not match the character in the word at `cur_word_ind`, return `False`.
   - **Mark the Current Cell as Visited**:
     - Set `visited[row][col]` to `True` to mark the current cell as visited.
   - **Recursively Explore Neighboring Cells**:
     - Recursive calls are made to explore the neighboring cells (top, right, bottom, left) to find the next character of the word.
     - Each recursive call increments `cur_word_ind` to move to the next character in the word.
   - **Backtracking**:
     - Before returning, mark the current cell as unvisited by setting `visited[row][col]` back to `False`.
   - **Return**:
     - If any of the recursive calls return `True`, indicating that the word has been found, return `True`.
     - If none of the recursive calls return `True`, return `False` to signify that the word cannot be formed starting from the current cell.

### Search for the Word:
#### Iterate Through Each Cell in the Board:
- Using two nested loops, iterate through each cell in the board:
  - Outer loop iterates over the columns (`j`) from `0` to `col_max - 1`.
  - Inner loop iterates over the rows (`i`) from `0` to `row_max - 1`.
- If the character in the current cell matches the first character of the word:
  - Call `find_word` with the current cell coordinates `(i, j)` and `cur_word_ind` set to `0`.
  - If `find_word` returns `True`, indicating that the word is found starting from the current cell, return `True` immediately.
- If the word is not found after searching all possible starting cells, return `False`.


This recursive function effectively explores all possible paths starting from a given cell in the board to match the given word, while ensuring that each cell is visited at most once during the exploration process.
