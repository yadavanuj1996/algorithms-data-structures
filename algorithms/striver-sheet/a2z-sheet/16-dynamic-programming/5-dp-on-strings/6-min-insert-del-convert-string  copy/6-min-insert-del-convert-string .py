"""
Delete Operation for Two Strings

Problem Link:
https://leetcode.com/problems/delete-operation-for-two-strings/

Statement
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 
the same.

In one step, you can delete exactly one character in either string.

Constraints:
- 1 <= word1.length, word2.length <= 500
- word1 and word2 consist of only lowercase English letters.

Test Case:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0
        
        for j in range(m+1):
            dp[0][j] = 0

        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0 + max(dp[i-1][j], dp[i][j-1])
            
        lcs_len = dp[n][m]
        
        return (n - lcs_len) + (m - lcs_len)
        


    
                 
   