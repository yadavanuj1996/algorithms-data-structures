"""
TC: O(n)
SC: O(charset)
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l ,r = 0, 0
        char_freq = {}
        max_freq = 1
        size = len(s)
        is_window_len_changed = True

        while r < size:
            window_len = r - l + 1
            if is_window_len_changed:
                char_freq[s[r]] =  char_freq.get(s[r]) + 1 if char_freq.get(s[r]) else 1
                max_freq = char_freq[s[r]] if max_freq < char_freq[s[r]] else max_freq
            else:
                char_freq[s[l-1]] =  char_freq.get(s[l-1]) - 1

            if window_len - max_freq <= k:
                r += 1
                is_window_len_changed = True
            else:
                l += 1
                is_window_len_changed = False

        return r-l
