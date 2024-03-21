# Combination Sum III Algorithm Summary

## Objective:
Find all combinations of k numbers from the range 1 to 9 whose sum equals a given target number n.

## Algorithm:
1. **Input:** `k` (size of combinations), `n` (target sum).
2. **Initialize:** 
    - An empty list `result` to store the combinations.
3. **Define a Helper Function `combination_sum_3`:**
    - Parameters: `index` (current index), `sum` (remaining sum), `arr` (current combination).
    - Base Case:
        - If sum < 0 or length of `arr` exceeds `k`, return.
        - If `index` reaches 10, check if sum == 0 and length of `arr` == `k`. If true, append `arr` to `result`.
    - Recursively Call `combination_sum_3`:
        - Include the current number (index) and decrease sum by the current number. Add the current number to `arr`.
        - Exclude the current number and move to the next index.
4. **Invoke `combination_sum_3`:** 
    - Initial parameters: (1, n, empty list).
5. **Return:** `result` containing all valid combinations found.

## Approach:
- Use backtracking to explore all possible combinations.
- Recursively iterate through numbers from 1 to 9.
- At each step, either include or exclude the current number in the combination.
- Maintain a condition to limit the combination size and check if the sum equals the target.
- Return all valid combinations found.
