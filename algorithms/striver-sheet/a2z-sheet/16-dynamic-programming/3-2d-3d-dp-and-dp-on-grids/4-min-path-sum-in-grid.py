
"""
Minimum Path Sum

Problem Link:
https://leetcode.com/problems/minimum-path-sum/description/

Statement
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.


Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 200

Test Case:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

"""


"""
Time Complexity: O(N*M)    ,     it is O(m+1 * n+1)       
Space Complexity: O(M*N) + O((n-1) + (m-1)),       O((n-1) + (m-1)) is recursion stack space

"""
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[-1 for j in range(n)] for i in range(m)]

        def get_min_path_sum(i, j):
            if i >= m or j >= n:
                return float("inf")
            
            if i == m-1 and j == n-1:
                return grid[i][j]
            
            if not memo[i][j] == -1:
                return memo[i][j]
            
            memo[i][j] = grid[i][j]+ min(get_min_path_sum(i, j+1), get_min_path_sum(i+1, j))
            return memo[i][j]
        
        return get_min_path_sum(0, 0)

        