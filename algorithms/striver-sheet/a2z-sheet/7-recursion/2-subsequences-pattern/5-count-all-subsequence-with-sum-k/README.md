
![IMG_7205](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/b5daca94-9dc7-41f2-8a58-6d522d1b0787)

## Prefix Sum approach (optimized)

### Algorithm Summary:

1. **Initialization:** Initialize variables `pre_sum` to track the prefix sum, `old_pre_sums` as a dictionary to store previously encountered prefix sums along with their indices, and `result` as an empty list to store the resulting subarrays.
2. **Prefix Sum Calculation:** Compute the prefix sum by adding the current element `a[i]` to the previous prefix sum `pre_sum`.
3. **Check for Subarrays with Sum `k`:**
    - If `pre_sum - k` exists in `old_pre_sums`, it implies that there exists a subarray whose sum equals `k`. Append this subarray, ranging from the index after the previous occurrence of `pre_sum - k` up to the current index `i`, to the `result` list.
4. **Update `old_pre_sums`:** Update the `old_pre_sums` dictionary with the current prefix sum `pre_sum` and its corresponding index `i`.
5. **Return Result:** Return the list of resulting subarrays.

This algorithm efficiently finds all subarrays with the desired sum `k` by maintaining a prefix sum and utilizing a dictionary to store previously encountered prefix sums along with their indices. It has a time complexity of O(n), where n is the size of the input array, making it an effective solution for the problem.



## Recursion based two pointer approach

### Algorithm Summary:

1. **Initialization:** Initialize an empty list to store the resulting subarrays.
2. **Recursive Function:** Define a recursive function, `subarray_with_sum_k`, to find subarrays with the desired sum recursively.
3. **Start Recursion:** Begin the recursion with the initial parameters: `start` and `end` both set to 0, and `sum` initialized to the value of the first element of the array.
4. **Recursive Steps:**
    - **Base Case:** If either `start` or `end` is beyond the array bounds, return.
    - **Check Sum:** If the current sum is less than or equal to the target sum `k`, check if it equals `k`. If so, append the subarray to the result list.
    - **Recursion:** Recursively call the function with updated parameters:
        - If the sum is less than or equal to `k`, increment `end` to include the next element in the subarray and update the sum accordingly.
        - If the sum exceeds `k`, increment `start` to exclude elements from the subarray until the sum is within the desired range.
5. **Return Result:** Return the resulting list of subarrays.

This algorithm efficiently finds all subarrays with the desired sum by recursively exploring all possible subarrays starting from each element in the array. The use of recursion and efficient updates of the start and end pointers ensure that the time complexity remains O(n), where n is the size of the input array, making it an effective approach for solving the problem.


