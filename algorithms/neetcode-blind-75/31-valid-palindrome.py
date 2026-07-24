"""
TC: O(n)
SC: O(n)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""

        for ch in s:
            if (ord(ch) >= ord("a") and ord(ch) <= ord("z")) or (ch in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]):
                new_s += ch

        print(new_s)
        start_index, last_index = 0, len(new_s) -1

        while start_index <= last_index:
            if new_s[start_index] != new_s[last_index]:
                return False

            start_index += 1
            last_index -= 1

        return True
