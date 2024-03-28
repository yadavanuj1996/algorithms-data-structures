"""
Reverse Words in a String

Problem Link:
https://leetcode.com/problems/reverse-words-in-a-string/

Statement:
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string
should only have a single space separating the words. Do not include any extra spaces.


Constraints:
- 1 <= s.length <= 10^4
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.


Test Case:

Input: s = "the sky is blue"
Output: "blue is sky the"

"""

"""
Time Complexity: 
Space Complexity: 
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        n = len(s)
        start, end = n-1, n-1
        for i in range(n-1, -1, -1):
            if start == end and s[i] == " ":
                start -= 1
                end = start
                continue

            if s[i] == " ":
                res += s[start+1:end+1] + " "
                end = start-1
            
            start -= 1
        
        res += s[start+1:end+1]

        return res
            

             


