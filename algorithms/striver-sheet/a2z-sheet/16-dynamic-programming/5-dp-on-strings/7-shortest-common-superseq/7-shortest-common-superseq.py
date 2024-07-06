"""
Shortest Common Supersequence

Problem Link:
https://leetcode.com/problems/shortest-common-supersequence/

Statement
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. 
If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results
in the string s.


Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of lowercase English letters.

Test Case:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"

Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0
        
        for j in range(m+1):
            dp[0][j] = 0
        
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        res = ""
        
        i,j = n, m
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                res = str1[i-1] + res
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] >= dp[i][j-1]:
                    res = str1[i-1] + res
                    i -= 1
                elif dp[i-1][j] < dp[i][j-1]:
                    res = str2[j-1] + res
                    j-= 1

        while i > 0:
            res = str1[i-1] + res
            i -= 1
        
        while j > 0:
            res = str2[j-1] + res
            j -= 1

        return res