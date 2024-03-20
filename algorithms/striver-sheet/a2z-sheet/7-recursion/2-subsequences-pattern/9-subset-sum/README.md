**Algorithm Summary:**

This is simple implementation of pick/ unpick approach.

1. **Inputs:** A list of integers `num`.
2. **Outputs:** A list of integers representing subset sums.
3. **Initialization:** 
    - `n`: Length of the input list `num`.
    - `result`: List to store subset sums.
4. **Helper Function `sum_of_subset`**:
    - Parameters: `index`, `num`, `sum`.
    - Base Case: If `index` equals `n`, append the current sum to `result` and return.
    - Recursively call `sum_of_subset`:
        - Pick the current element (`num[index]`) and add it to the current sum.
        - Don't pick the current element (`num[index]`) and continue.
5. **Call `sum_of_subset(0, num, 0)`** to start generating subset sums.
6. **Sort the `result` list**.
7. **Return the sorted `result` list**.

This algorithm utilizes a recursive approach to generate all possible combinations of subset sums.
