from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [-1]*n

        def word_break(index):
            if index == n:
                return True

            if memo[index] != -1:
                return memo[index]

            result = False
            for word in wordDict:
                word_len = len(word)
                if s[index: index+word_len] == word:
                    # pick
                    result = result or word_break(index+word_len)

            memo[index] = result
            return result

        return word_break(0)
