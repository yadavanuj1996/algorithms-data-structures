"""
Longest Common Subsequence

Problem Link:
https://leetcode.com/problems/longest-common-subsequence

Statement
Given two strings text1 and text2, return the length of their longest common subsequence. If 
there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters
(can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.


Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

Test Case:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

"""


"""
Time Complexity: O(N*M) 
Space Complexity: O(N*M) + O(N+M) , O(N*M) for dp array, O(N+M) for auxillary stack space

"""
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