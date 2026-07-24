"""
TC: O(m + n)
SC: O(charset)
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        size = len(s)
        result = ""
        result_len = float("inf")
        l, r = 0, 0
        required_chars = {}
        window = {}
        required_len = len(t)
        current_len = 0
        is_new_char_added_in_window = True
        for curr_char in t:
            required_chars[curr_char] = 1 + required_chars.get(curr_char, 0)
            window[curr_char] = 0

        while r < size and l <= r:
            if s[r] in t and is_new_char_added_in_window:
                window[s[r]] += 1
                if window[s[r]] <= required_chars[s[r]]:
                    current_len += 1

            #print(required_len, current_len, window)
            if required_len == current_len:
                curr_substring = s[l:r+1]
                if len(curr_substring) < result_len:
                    result = curr_substring
                    result_len = len(curr_substring)
                    #print(result)

                if not required_chars.get(s[l]):
                    l += 1
                    is_new_char_added_in_window = False
                    continue

                if window[s[l]] > required_chars[s[l]]:
                    window[s[l]] -= 1
                    l += 1
                    is_new_char_added_in_window = False
                    continue

                window[s[l]] -= 1
                current_len -= 1
                l += 1
                is_new_char_added_in_window = True

            r += 1

        return result
