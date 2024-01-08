
"""
Unique Paths

Problem Link:
https://leetcode.com/problems/unique-paths/description/

Statement
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to
reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

Constraints:
- 1 <= m, n <= 100

Test Case:

Input: m = 3, n = 2

Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""


"""
Time Complexity: O(N*M)    ,     it is O(m+1 * n+1)       
Space Complexity: O(M*N) + O((n-1) + (m-1)),       O((n-1) + (m-1)) is recursion stack space

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

        return get_unique_paths(0,0)
