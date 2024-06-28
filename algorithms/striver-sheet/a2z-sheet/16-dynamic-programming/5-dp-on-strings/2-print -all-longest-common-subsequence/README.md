## NOTE: README and Problem solved is different
In the README i have solved the original problem of printing LCS (longest common subsequence), if 
there are multiple LCS of same length print any. 

While in python code i have solved the problem for printing all the possible LCS (The code is not
most efficient as it did run TLE for some test cases but i did not improved as it was not the 
original problem.)

### Algorithm Summary:

The algorithm finds the longest common subsequence (LCS) between two strings `s` and `t` using dynamic programming (DP).

1. **Initialization**:
   - Create a 2D DP array `dp` of size `(n+1) x (m+1)` where `n` is the length of string `s` and `m` is the length of string `t`. Initialize all elements to -1.
   - Set the first row and first column of the `dp` array to 0. This handles the base case where the LCS length is 0 if one of the strings is empty.

2. **Filling the DP Table**:
   - Iterate over the characters of both strings `s` and `t` using nested loops.
   - If the characters match, set `dp[i][j]` to `1 + dp[i-1][j-1]`.
   - If they do not match, set `dp[i][j]` to `max(dp[i-1][j], dp[i][j-1])`.
   - This step computes the length of the LCS and fills the DP table accordingly.

3. **Backtracking to Find the LCS**:
   - Start from the bottom-right corner of the DP table.
   - If characters match, add the character to the result and move diagonally up-left in the DP table.
   - If characters do not match, move in the direction of the higher DP value.
   - Continue this process until the top-left corner is reached.

4. **Return the LCS**:
   - The constructed LCS is stored in the `res` string, which is returned as the result.

### Time Complexity:
- **Filling the DP Table**: \(O(n \times m)\), where \(n\) is the length of string `s` and \(m\) is the length of string `t`.
- **Backtracking to Find the LCS**: \(O(n + m)\), as it involves a single traversal from the bottom-right to the top-left corner of the DP table.

### Space Complexity:
- **DP Table**: \(O(n \times m)\), due to the storage required for the 2D DP array.
- **Auxiliary Space**: \(O(1)\), as no additional space is used other than the DP table and the result string.

```python
class Solution:
    def all_longest_common_subsequences(self, s, t):
        # dp[i][j] represents value of common subsequence between two strings
        # for first string text1 (0 -> i) index and for second string text2 (0 -> j)
        text1 = s
        text2 = t
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
        
        # Step1: Set up base that i.e., for 0th row and 0th col the dp val will be 0 (shifting the -ve to 0 index by 1)
        for ind in range(n+1):
            dp[ind][0] = 0

        for ind in range(m+1):
            dp[0][ind] = 0

        # Step 2: iterate over the indexes in reverse order
        # We are starting from 1 as we have shifted indexes and took -1 to 0, 0 to 1 so on
        for i in range(1, n+1):
            for j in range(1, m+1):
                # Step 3: Copy the recurrence
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0 + max(dp[i-1][j], dp[i][j-1])

        res = ""
        row, col = n, m
        
        while row > 0 and col > 0:
            if text1[row-1] == text2[col-1]:
                res = text1[row-1] + res
                row -= 1
                col -= 1
            else:
                if dp[row-1][col] > dp[row][col-1]:
                    row -= 1
                else:
                    col -= 1
        
        return res
```