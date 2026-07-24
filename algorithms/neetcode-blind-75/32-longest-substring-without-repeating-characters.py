"""
TC: O(n)
SC: O(min(n, charset))
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result_len = 0
        l,r = 0, 0
        curr_char = {}
        size = len(s)

        while r < size :
            curr_char[s[r]] = curr_char.get(s[r], 0) + 1
            while curr_char[s[r]] > 1:
                curr_char[s[l]] -= 1
                l += 1


            if result_len < r-l+1 :
                result_len = r-l+1

            r += 1

        return result_len
