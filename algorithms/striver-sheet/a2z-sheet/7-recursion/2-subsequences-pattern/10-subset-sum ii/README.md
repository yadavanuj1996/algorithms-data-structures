## Algorithm: Subsets with Duplicates

1. **Input**: A list of integers `nums`.
2. Initialize an empty list `result` to store the subsets.
3. Get the length of the input list `n`.
4. Sort the input list `nums`.
5. Define a recursive function `get_subset_with_dup(index, arr)` to generate subsets with duplicates:
    - Base case: If `index` reaches `n`, append the current subset `arr` to `result`.
    - Pick the current element at `index` and recurse by calling `get_subset_with_dup(index + 1, arr + [nums[index]])`.
    - Unpick the current element if there are duplicates:
        - Increment `index` as long as the next element is a duplicate.
    - Recurse without picking the current element by calling `get_subset_with_dup(index + 1, arr)`.
6. Start recursion with initial parameters `get_subset_with_dup(0, [])`.
7. Return the `result` list containing all generated subsets with duplicates.
