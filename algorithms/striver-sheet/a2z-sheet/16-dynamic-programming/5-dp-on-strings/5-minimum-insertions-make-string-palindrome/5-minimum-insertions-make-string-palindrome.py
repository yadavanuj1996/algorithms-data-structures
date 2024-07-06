"""
Minimum Insertion Steps to Make a String Palindrome

Problem Link:
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

Statement
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.


Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters.

Test Case:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.


Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
"""


"""
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        # longest palindromic subsequence can be calculated with taking a string and it's reverse
        # and finding the longest common subsequence between them
        s_rev = ""
        for i in range(n-1, -1, -1):
            s_rev += s[i]

        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(n):
            dp[i][0] = 0
            dp[0][i] = 0
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s_rev[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        long_palind_subseq_len = dp[n][n]
    
        # if you carefully observe to calculate total no of insertions in a string to make it 
        # palindrome we simply need to find the current longest palindromic subsequence in the 
        # given string and keep it as it is and for the rest of the characters we need to insert
        # those characters one more time in string to make the string palindrome
        return n - long_palind_subseq_len
        