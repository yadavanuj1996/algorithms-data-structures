"""
TC: O(n * m)
SC: O(n * m) (memo) + O(n + m) recursion stack
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def lcs(index_1, index_2):
            if index_1 == -1 or index_2 == -1:
                return 0

            if dp[index_1][index_2] != -1:
                #print(dp[index_1][index_2])
                return dp[index_1][index_2]

            pick, not_pick = 0, 0
            # pick
            if text1[index_1] == text2[index_2]:
                pick = 1 + lcs(index_1 - 1, index_2 - 1)
            # not pick
            else:
                left_move_ahead = lcs(index_1 - 1, index_2)
                right_move_ahead = lcs(index_1, index_2 - 1)

                not_pick = max(left_move_ahead, right_move_ahead)

            dp[index_1][index_2] = max(pick, not_pick)
            return dp[index_1][index_2]

        lcs(n-1, m-1)

        return dp[n-1][m-1]
