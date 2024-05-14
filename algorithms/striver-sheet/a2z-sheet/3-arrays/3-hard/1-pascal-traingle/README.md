![Screenshot 2024-05-14 at 6 01 58 PM](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/9c056c0f-34e1-4f3a-9846-ff8b6aaa22ee)

This algorithm generates a Pascal's Triangle up to a specified number of rows (`numRows`). Here's a summary of how it works:

1. Initialize an empty list `res` to store the rows of Pascal's Triangle.
2. Iterate over each row index `r` from `0` to `numRows-1`.
3. For each row `r`:
   - Start by appending a list containing `[1]` to `res`, representing the first element of the current row (which is always `1`).
   - Initialize `ans` to `1`, which will hold the current calculated value.
   - Iterate over each column index `c` from `1` to `r` (since the first value is always `1` and already appended):
     - Update `ans` by multiplying it with `(r-c+1)` (equivalent to calculating factorial values).
     - Then, divide `ans` by `c` (also part of factorial computation) to get the specific value for the current position `(r, c)` in Pascal's Triangle.
     - Append `ans` to the current row in `res`.
4. Return the completed Pascal's Triangle (`res`) after generating all required rows.

This algorithm efficiently computes each element of Pascal's Triangle using factorials to determine binomial coefficients. The result is returned as a list of lists, representing each row of the triangle up to the specified number of rows (`numRows`).
