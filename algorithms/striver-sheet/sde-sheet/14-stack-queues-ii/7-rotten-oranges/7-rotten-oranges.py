"""
Rotting Oranges

Problem Link:
https://leetcode.com/problems/rotting-oranges/

Statement:
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible,
return -1.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2.

Test Case:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

"""
"""
Time Complexity: O(m*n), Reason: Worst-case – We will be making each fresh orange rotten in the grid and for each rotten orange will check in 4 directions
Space Complexity: O(m*n), visited has m*n size or if all oranges are Rotten, we will end up pushing all rotten oranges into the Queue data structure
"""
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = deque()
        m = len(grid)
        n = len(grid[0])
        visited = [[False if grid[i][j] == 1 else True for j in range(n)] for i in range(m)]
        total_oranges = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    total_oranges += 1
                    dq.append((i,j,0))
                    
                if grid[i][j] == 1:
                    total_oranges += 1

        cur_time = 0
        total_queue_items = 0

        while dq:
            i, j, time = dq.popleft()
            cur_time = time
            total_queue_items += 1
            # top
            self.add_fresh_tomatoes_queue(dq, i-1, j, visited, m, n, cur_time)
            # right
            self.add_fresh_tomatoes_queue(dq, i, j+1, visited, m, n, cur_time)
            # bottom
            self.add_fresh_tomatoes_queue(dq, i+1, j, visited, m, n, cur_time)
            # left
            self.add_fresh_tomatoes_queue(dq, i, j-1, visited, m, n, cur_time)
        
        return cur_time if total_oranges == total_queue_items else -1
            
            
    def add_fresh_tomatoes_queue(self, dq, row_index, col_index, visited, m, n, cur_time):
        if row_index >= 0 and row_index < m and col_index >= 0 and col_index < n and \
            not visited[row_index][col_index]:
            visited[row_index][col_index] = True
            dq.append((row_index, col_index, cur_time+1))


    
        


        