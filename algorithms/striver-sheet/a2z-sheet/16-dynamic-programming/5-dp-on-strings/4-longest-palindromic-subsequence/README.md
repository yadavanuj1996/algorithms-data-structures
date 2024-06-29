## Longest Palindromic Subsequence Algorithm

### Summary
The algorithm to find the longest palindromic subsequence in a given string is based on the concept that a palindrome reads the same forwards and backwards. Therefore, the longest palindromic subsequence in a string can be found by determining the longest common subsequence (LCS) between the string and its reversed version.

### Algorithm

1. **Reverse the String:**
   - Create a reversed version of the input string `s` named `s_rev`.

2. **Initialize the DP Table:**
   - Create a 2D list `dp` with dimensions `[len(s) + 1][len(s_rev) + 1]`, initialized to `0`, to store the length of the longest common subsequence for substrings of `s` and `s_rev`.

3. **Fill the DP Table:**
   - Iterate through each character of `s` and `s_rev`.
     - If the characters at the current indices of `s` and `s_rev` are equal, the value at `dp[i][j]` is `1 + dp[i-1][j-1]`.
     - Otherwise, the value at `dp[i][j]` is the maximum of `dp[i-1][j]` and `dp[i][j-1]`.

4. **Result:**
   - The length of the longest palindromic subsequence is found at `dp[len(s)][len(s_rev)]`.

### Why Reverse the String?
Reversing the string allows us to leverage the longest common subsequence (LCS) algorithm. Since a palindromic subsequence reads the same forwards and backwards, finding the LCS between the original string and its reverse effectively identifies the longest subsequence that is palindromic.

### Time and Space Complexity
- **Time Complexity (TC):** O(n^2), where n is the length of the input string. This is due to the nested loops used to fill the DP table.
- **Space Complexity (SC):** O(n^2), for the storage of the DP table.

### Code Implementation

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        This function computes the length of the longest palindromic subsequence
        in the given string 's'. A palindromic subsequence is a sequence that
        reads the same forwards and backwards. To find this, the function uses
        the longest common subsequence (LCS) method between 's' and its reversed
        version 's_rev'.
        """
        # Reverse the input string
        s_rev = ""
        for i in range(len(s)-1, -1, -1):
            s_rev += s[i]
        
        n = len(s)
        m = len(s_rev)

        # Initialize a DP table with -1
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

        # Set the base cases: LCS with an empty string is 0
        for i in range(n+1):
            dp[i][0] = 0
        for j in range(m+1):
            dp[0][j] = 0
        
        # Fill the DP table
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == s_rev[j-1]:  # If characters match, add 1 to the result of the previous indices
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:  # If characters do not match, take the maximum from previous index in either string
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # The bottom-right cell contains the length of the longest palindromic subsequence
        return dp[n][m]
```

