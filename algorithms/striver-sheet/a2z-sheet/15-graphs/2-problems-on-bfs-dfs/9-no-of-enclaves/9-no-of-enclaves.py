"""
Number of Enclaves

Problem Link:
https://leetcode.com/problems/number-of-enclaves/

Statement
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking 
off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number 
of moves.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 500
- grid[i][j] is either 0 or 1.


Test Case:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3

Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

"""

"""
Time Complexity: O(N*M),  actually  O(N*M) (visited arr set) + O(N) (for loop) + O(M) (for loop) + O(N * M * 4) (recursion calls of dfs) + O(N*M) (nested for loops)
Space Complexity: O(N*M) ,  actually O(2*N*M) -> recursion stack space and visited array 
"""
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        total_rows = len(grid)
        total_cols = len(grid[0])
        is_visited = [[False for _ in range(total_cols)] for _ in range(total_rows)]
        # DFS function taht calls all the adj land cells having value 1
        def mark_border_con_land_cell(row, col):
            if row < 0 or row >= total_rows or col < 0 or col >= total_cols or grid[row][col] == 0 or \
            is_visited[row][col]:
                return 

            is_visited[row][col] = True

            # top
            mark_border_con_land_cell(row-1, col)
            # right
            mark_border_con_land_cell(row, col+1)
            # bottom
            mark_border_con_land_cell(row+1, col)
            # left
            mark_border_con_land_cell(row, col-1)

        # first and last row
        for c in range(total_cols):
            if grid[0][c] == 1:
                mark_border_con_land_cell(0, c)
            if grid[total_rows-1][c] == 1:
                mark_border_con_land_cell(total_rows-1, c)

        # first and last col
        for r in range(total_rows):
            if grid[r][0] == 1:
                mark_border_con_land_cell(r, 0)
            if grid[r][total_cols-1] == 1:
                mark_border_con_land_cell(r, total_cols-1)
    
        result = 0           # total non boundary connected land cells
        for r in range(total_rows):
            for c in range(total_cols):
                if grid[r][c] == 1 and not is_visited[r][c]:
                    result += 1

        return result


        

