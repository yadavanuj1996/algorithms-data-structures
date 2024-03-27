"""
Rotate String

Problem Link:
https://leetcode.com/problems/rotate-string/

Statement:
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.


Constraints:
- 1 <= s.length, goal.length <= 100
- s and goal consist of lowercase English letters.


Test Case:

Input: s = "abcde", goal = "cdeab"
Output: true

"""

"""
Time Complexity: O(2N), N is length of string s
Space Complexity: O(N)
"""
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) < len(s):
            return False

        s += s[:-1]
        return goal in s
        