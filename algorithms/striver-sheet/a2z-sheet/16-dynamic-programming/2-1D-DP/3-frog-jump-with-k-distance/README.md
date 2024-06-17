## minimizeCost Algorithm

The `minimizeCost` function calculates the minimum energy required for a frog to jump to the last stone, given an array of stone heights and the maximum number of stones the frog can jump over at once.

### Algorithm

1. **Initialization:**
   - Create a memoization array `memo` of size `n` initialized with `-1`.
   - Base cases: 
     - `memo[0]` is `0` because no energy is needed to stay on the first stone.
     - `memo[1]` is the absolute difference between the heights of the first and second stones.

2. **Iterative Calculation:**
   - For each stone from the third to the nth stone:
     - Calculate the minimum energy required to reach the current stone by considering all possible jumps from previous stones within the allowed range (up to `k` stones).

3. **Result:**
   - The minimum energy required to reach the last stone is stored in `memo[n-1]`.

### Pseudocode

```python
def minimizeCost(n : int, k : int, heights : List[int]) -> int:
    # Write your code here.
    memo = [-1]*n

    def min_energy_req(n):
        if n == 1:
            return 0

        memo[0] = 0
        memo[1] = abs(heights[1] - heights[0])
        for i in range(2, n):
            for j in range(i, k)
            memo[i] = min(
                abs(heights[i] - heights[i-1]) + memo[i-1], 
                abs(heights[i] - heights[i-2]) + memo[i-2]
                )

        return memo[n-1]

```

### Time Complexity

The time complexity of this algorithm is **O(n * k)**, where `n` is the number of stones and `k` is the maximum number of stones the frog can jump over at once. This is because for each stone (from 2 to n), the algorithm checks up to `k` previous stones to calculate the minimum energy required.

### Space Complexity

The space complexity of this algorithm is **O(n)** due to the memoization array `memo` used to store the minimum energy required to reach each stone.

