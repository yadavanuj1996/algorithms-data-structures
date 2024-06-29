## Algorithm Summary: Longest Common Substring

### Description
The `longestCommonSubstr` function finds the length of the longest common substring between two given strings `S1` and `S2`. This is an extension of the Longest Common Subsequence (LCS) problem with the key difference that if characters do not match, we reset the length of the common substring to zero.

### Algorithm
1. **Initialize a DP Table**: Create a 2D list `dp` with dimensions `(n+1) x (m+1)` initialized to -1. Here, `n` and `m` are the lengths of `S1` and `S2` respectively.
2. **Base Case**: Set the first row and first column of `dp` to 0 to represent comparisons with empty substrings.
3. **Fill DP Table**:
    - Iterate through each character in `S1` and `S2`.
    - If characters match (i.e., `S1[i-1] == S2[j-1]`), it means we can extend the common substring found up to the previous indices. Thus, update `dp[i][j]` to `1 + dp[i-1][j-1]`. Here, `dp[i-1][j-1]` represents the length of the longest common substring ending at the previous characters of `S1` and `S2`.
    - If characters do not match (i.e., `S1[i-1] != S2[j-1]`), it means the common substring is broken at these indices, so set `dp[i][j]` to 0. This signifies that there is no common substring ending at these indices.
    - Keep track of the maximum value in the `dp` table, which represents the length of the longest common substring.
4. **Result**: Return the maximum value found in the `dp` table.

### Time Complexity (TC)
The time complexity of this algorithm is `O(n * m)` because we are iterating through each character of both strings, filling out a 2D table of size `(n+1) x (m+1)`.

### Space Complexity (SC)
The space complexity is also `O(n * m)` due to the storage requirement for the 2D list `dp`.

### Code Snippet

- dp[i][j] array represents common substring ending at these indices (S1 -> i index, S2 -> j index).

```python
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        res = 0
        # Initialize dp table
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]    
        
        # Base case: dp[i][0] and dp[0][j] should be 0
        for i in range(n):
            dp[i][0] = 0
        
        for j in range(m):
            dp[0][j] = 0
        
        # Fill dp table
        for i in range(1, n+1):
            for j in range(1, m+1):
                if S1[i-1] == S2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]  # Extend the common substring length
                else:
                    dp[i][j] = 0  # No common substring at these indices
                
                res = max(res, dp[i][j])
        
        return res
```
