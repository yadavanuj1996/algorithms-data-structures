"""
Shortest Path in Binary Matrix

Problem Link:
https://leetcode.com/problems/shortest-path-in-binary-matrix/

Statement
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there 
is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right 
cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they 
share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Constraints:
- n == grid.length
- n == grid[i].length
- 1 <= n <= 100
- grid[i][j] is 0 or 1


Test Case:

Input: grid = [[0,1],[1,0]]
Output: 2

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
"""

"""
Approach: We are solving this problem using graph BFS algorithm, here we have taken (0,0) as source node
and (no_of_rows-1, no_of_cols-1) as destination node.

Time Complexity: O(8*N*M),  N and M are total no of rows and cols , as we are checking all 8 adjacent nodes
Space Complexity: O(N*M),   N and M are total no of rows and cols
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        no_of_rows = len(grid)
        no_of_cols = len(grid[0])
        queue = []
        visited = [[False for _ in range(no_of_cols)] for _ in range(no_of_rows)]
        # if source node or destination node is 1 return -1
        if grid[0][0] == 1 or grid[no_of_rows-1][no_of_cols-1] == 1:
            return -1

        queue.append((0, 0, 0))

        while queue:
            row, col, dist = queue.pop(0)

            if row < 0 or row >= no_of_rows or col < 0 or col >= no_of_cols or grid[row][col] == 1 or visited[row][col]:
                continue
            
            visited[row][col] = True
            
            # we are returning dist + 1 because the no of cells are no_of_edges + 1
            if row == no_of_rows-1 and col == no_of_cols-1:
                return dist + 1

            # top
            queue.append((row-1, col, dist+1))
            # top right
            queue.append((row-1, col+1, dist+1))
            # right
            queue.append((row, col+1, dist+1))
            # right bottom
            queue.append((row+1, col+1, dist+1))
            # bottom
            queue.append((row+1, col, dist+1))
            # bottom left
            queue.append((row+1, col-1, dist+1))
            # left
            queue.append((row, col-1, dist+1))
            # left top
            queue.append((row-1, col-1, dist+1))
            

        
        return -1