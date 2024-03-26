"""
Reverse Words in a String

Problem Link:
https://leetcode.com/problems/reverse-words-in-a-string/description/

Statement:
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned 
string should only have a single space separating the words. Do not include any extra spaces.


Constraints:
- 1 <= s.length <= 10^4
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.

Test Case:

Input: s = "the sky is blue"
Output: "blue is sky the"

"""

"""
Time Complexity: O(N)
Space Complexity: O(N)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        n = len(s)
        start, end = 0, 0
        while start < n:
            if s[start] == " ":
                start += 1
                end = start
                continue
        
            while not (end == n or s[end] == " "):
                end += 1
            
            res = s[start:end] + " "+ res
            start = end
        
        return res[:-1]


        