"""
Time Complexity: O(M+N), M is length of s and N is length of t
Space Complexity: O(M+N),
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        s_freq = {}
        t_freq = {}

        for ch in s:
            s_freq[ch] = s_freq[ch]+1 if s_freq.get(ch) else 1

        for ch in t:
            t_freq[ch] = t_freq[ch]+1 if t_freq.get(ch) else 1

        return s_freq == t_freq
