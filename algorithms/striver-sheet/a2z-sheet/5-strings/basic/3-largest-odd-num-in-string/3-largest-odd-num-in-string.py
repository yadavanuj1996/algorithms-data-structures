"""
Largest Odd Number in String

Problem Link:
https://leetcode.com/problems/largest-odd-number-in-string/

Statement:
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) 
that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.


Constraints:
- 1 <= num.length <= 10^5
- num only consists of digits and does not contain any leading zeros.


Test Case:

Input: num = "52"

Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
"""

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            # an number is simply an odd no if the last digit of the number is odd
            if int(num[i]) % 2 == 1:
                return num[0:i+1]

        return ""
        