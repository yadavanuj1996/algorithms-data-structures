"""
Longest Common Prefix

Problem Link:
https://leetcode.com/problems/longest-common-prefix/

Statement:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.


Test Case:

Input: strs = ["flower","flow","flight"]
Output: "fl"

"""

"""
Time Complexity: O(m * n),   n represents the length of the longest string in the input list strs. m represents the number of strings in the list strs.
Space Complexity: O(1)
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i in range(len(strs[0])):
            fir_elem_char = strs[0][i]
            is_further_processing_req = True

            ind = 1
            while ind < len(strs):
                if i >= len(strs[ind]):
                    is_further_processing_req = False
                    break

                if not strs[ind][i] == fir_elem_char:
                    is_further_processing_req = False
                    break
                
                ind += 1

            if not is_further_processing_req:
                break
            else:
                result += fir_elem_char
        
        return result
        


