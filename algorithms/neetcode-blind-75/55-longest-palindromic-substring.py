class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        n = len(s)

        def expand(left_index, right_index):
            while left_index >= 0 and right_index < n and s[left_index] == s[right_index]:
                left_index -= 1
                right_index += 1
            # this will return the most possible expanded string
            return s[left_index+1: right_index]

        for i in range(n):
            odd = expand(i, i)
            even = expand(i, i+1)

            if len(odd) > len(result):
                result = odd

            if len(even) > len(result):
                result = even

        return result
