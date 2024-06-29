"""
Longest Common Substring

Problem Link:
https://www.geeksforgeeks.org/problems/longest-common-substring1452/1

Statement
Given two strings. The task is to find the length of the longest common substring.

Constraints:
- 1<=n, m<=1000

Test Case:

Input: S1 = "ABCDGH", S2 = "ACDGHR", n = 6, m = 6
Output: 4

Explanation: The longest common substring
is "CDGH" which has length 4.
"""


"""
Time Complexity: O(N*M) 
Space Complexity: O(N*M) 

"""
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        res = 0
        # initialize dp
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]    
        # Extension of LCS problem with a twist that if the characters
        # do not match we do not need to go back to look for old indexes
        # and dp value will start with 0
        
        # Step 1: set base case for dp for row and col to 0 as they will represent 
        # negative indexes (i, j) for S1 & S2 the dp value of substring
        # will be stored in (i+1, j+1)
    
        for i in range(n):
            dp[i][0] = 0
        
        for j in range(m):
            dp[0][j] = 0
        
        # Step 2: Iterate over indexes in reverse order
        for i in range(1, n+1):
            for j in range(1, m+1):
                if S1[i-1] == S2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0
                
                res = max(res, dp[i][j])
        
        return res
    
                 
   