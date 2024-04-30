""" 
Find the Index of the First Occurrence in a String

Problem Link:
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Statement
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if 
needle is not part of haystack.


Constraints:
- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English characters.

Test Case:
Sample Input 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Sample Input 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

"""
Approach: Using Z algorithm

Time Complexity: O(m +n) 
Space Complexity: O(m +n)
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        comb_str = needle + "$" + haystack
        n = len(comb_str)
        l, r = 0, 0
        z = [0] * n

        for i in range(1, n):
            if i > r:
                l, r = i, i 

                while r < n and comb_str[r-l] == comb_str[r]:
                    r += 1
                
                z[i] = r - l
                r -= 1
            else:
                correspond_start_index = i - l
                # if the current index i + z[cors_s_i] is greater than r means that the z[i] val
                # goes out of current selected window then we need to compare indexes out of the
                # current selected window
                if i + z[correspond_start_index] < r+1:
                    z[i] = z[correspond_start_index]
                else: 
                    # decreasing the window size by updating l to i
                    l = i
                    while r < n and comb_str[r-l] == comb_str[r]:
                        r += 1
                
                    z[i] = r - l
                    r -= 1
        
        needle_len = len(needle)
        
        for i in range(len(z)):
            if z[i] == needle_len:
                # note we have merged the needle and haystack string so we need to remove the 
                # len of needle and special character $ len
                return i - (needle_len+1)

        return -1