## Longest Common Subsequence Algorithm

The `longestCommonSubsequence` function calculates the length of the longest common subsequence between two given strings `text1` and `text2`.

### Algorithm

1. **Initialization:**
   - Create a 2D list `dp` with dimensions `[len(text1)][len(text2)]`, initialized to `-1`, to store the length of the longest common subsequence for substrings of `text1` and `text2`.

2. **Recursive Function (`longest_common_subseq`):**
   - Base cases:
     - If either `str_1_index` or `str_2_index` is less than `0`, return `0` because an empty string has no common subsequence.
     - If the value at `dp[str_1_index][str_2_index]` is already calculated, return that value to avoid redundant calculations.
   - Recursively calculate the length of the longest common subsequence:
     - If the characters at the current indices of `text1` and `text2` are equal, the result is `1 + longest_common_subseq(str_1_index-1, str_2_index-1)`.
     - Otherwise, the result is the maximum of `longest_common_subseq(str_1_index-1, str_2_index)` and `longest_common_subseq(str_1_index, str_2_index-1)`.
   - The indices are reduced in the recursive function to progressively consider shorter substrings of `text1` and `text2`.

3. **Result:**
   - The length of the longest common subsequence of `text1` and `text2` is obtained by calling `longest_common_subseq(len(text1)-1, len(text2)-1)`.

### Code

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] represents value of common subsequence between two strings
        # for first string text1 (0 -> i) index and for second string text2 (0->j)
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        # To write recursion fn
        # Step 1: Define the problems in terms of all indexes
        # Step 2: For each index explore all possibilities 
        # Step 3: Find max/min/action of all indexes
        
        def longest_common_subseq(str_1_index, str_2_index):
            if str_1_index < 0 or str_2_index < 0:
                return 0
            
            if not dp[str_1_index][str_2_index] == -1:
                return dp[str_1_index][str_2_index]

            if text1[str_1_index] == text2[str_2_index]:
                dp[str_1_index][str_2_index] = 1 + longest_common_subseq(str_1_index-1, str_2_index-1) 
            else:
                dp[str_1_index][str_2_index] = max(
                    longest_common_subseq(str_1_index-1, str_2_index),
                    longest_common_subseq(str_1_index, str_2_index-1)
                )
            
            return dp[str_1_index][str_2_index]

        return longest_common_subseq(n-1, m-1)
```

### Time Complexity

The time complexity of this algorithm is **O(N * M)**, where `N` and `M` are the lengths of `text1` and `text2`, respectively. This is because we are computing the value for each pair of indices `(i, j)` exactly once.

### Space Complexity

The space complexity of this algorithm is **O(N * M)** for the `dp` array plus **O(N + M)** for the auxiliary stack space used by the recursion. Hence, the total space complexity is **O(N * M) + O(N + M)**.