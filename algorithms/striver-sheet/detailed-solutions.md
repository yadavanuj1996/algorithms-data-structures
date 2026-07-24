# Striver Sheet — Detailed Solutions

Detailed walkthrough of each problem: problem statement, the key trick, and the full solution.

---

## A2Z DSA Course Problems

### Arrays

#### 1. Find Second Largest Element

| Category | Pattern | Key Trick | Time | Space |
|----------|---------|-----------|------|-------|
| Array | Single Pass | Use two variables to track largest and second largest in one pass | O(n) | O(1) |

**Problem Statement:**
Given an array `Arr` of size `N`, print the second largest distinct element from the array. If the second largest element doesn't exist, return `-1`.

Constraints:
- `2 ≤ N ≤ 10^5`
- `1 ≤ Arr[i] ≤ 10^5`

Example:
```
Input:  N = 6, Arr[] = {12, 35, 1, 10, 34, 1}
Output: 34
Explanation: The largest element is 35 and the second largest distinct element is 34.
```

**Solution:**
```python
# Time: O(N) | Space: O(1)

def secondLargest(arr, n):
    if (n < 2):
        return -1

    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    return second_large
```

---
