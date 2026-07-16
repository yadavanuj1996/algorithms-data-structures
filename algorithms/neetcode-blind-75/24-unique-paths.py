"""
TC: O(m * n)
SC: O(m * n) memo + O(m + n) recursion stack
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for j in range(n)] for i in range(m)]

        def get_unique_paths(i, j):
            if i >= m or j >= n:
                return 0

            if i == m-1 and j == n-1:
                return 1

            if not memo[i][j] == -1:
                return memo[i][j]

            memo[i][j] = get_unique_paths(i+1, j) + get_unique_paths(i, j+1)
            return memo[i][j]

        return get_unique_paths(0, 0)
