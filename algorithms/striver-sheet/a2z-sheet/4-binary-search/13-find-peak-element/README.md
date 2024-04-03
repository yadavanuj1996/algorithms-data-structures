![Screenshot 2024-04-04 at 4 51 05 AM](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/aae00ce9-8e28-44d8-a0bb-e01224b078ea)

**Algorithm Summary: Finding Peak Element**

1. **Inputs:** A list of integers `nums`.
2. **Outputs:** The index of a peak element in the input list.
3. **Initialization:** 
    - `n`: Length of the input list `nums`.
    - `low`: Initialized to 1, representing the start index.
    - `high`: Initialized to `n-2`, representing the end index.
4. **Edge Case Handling:**
    - If `n == 1`, return 0 (only element is a peak).

    - If the first element is a peak, return 0.
    - If the last element is a peak, return `n-1`.
5. **Binary Search Algorithm:**
    - While `low` is less than or equal to `high`:
        - Calculate `mid` as `(low + high) // 2`.
        - If `nums[mid-1] < nums[mid] > nums[mid+1]`, return `mid` as peak.
        - If `nums[mid] > nums[mid+1]`, update `high = mid - 1`.
        - If `nums[mid] < nums[mid+1]`, update `low = mid + 1`.
6. **Termination:** The search terminates when `low` exceeds `high`.
