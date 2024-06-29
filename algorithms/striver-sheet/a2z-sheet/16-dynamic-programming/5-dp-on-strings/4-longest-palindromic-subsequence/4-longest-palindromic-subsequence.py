"""
Longest Palindromic Subsequence

Problem Link:
https://leetcode.com/problems/longest-palindromic-subsequence/

Statement
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements 
without changing the order of the remaining elements.


Constraints:
- 1 <= s.length <= 1000
- s consists only of lowercase English letters.

Test Case:

Ex 1:
Input: s = "bbbab"
Output: 4

Explanation: One possible longest palindromic subsequence is "bbbb".

Ex 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        If we reverse a palindrome string and compare it with original one from left to right
        it will be same, similarly if we have a palindrome subsequence in a sting and we reverse
        the string if we iterate over it left to right we will still find the palindrome 
        subsequence (in left to right pass) only.
        
        ex: org -> aebrba , reverse -> abrbea
        Note: a, ab, aba, abba are all palindorme subsequence that are present in 
        # both original and reverse string. Longest palindromc subsequence in a string
        will be a longest common subsequence between a string and it's reverse string.
        """
        s_rev = ""

        for i in range(len(s)-1, -1, -1):
            s_rev += s[i]
        
        n = len(s)
        m = len(s_rev)

        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0
        
        for j in range(m+1):
            dp[0][j] = 0
        
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == s_rev[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n][m]

    



    
                 
   