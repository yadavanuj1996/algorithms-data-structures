"""
01 Matrix

Problem Link:
https://leetcode.com/problems/01-matrix/

Statement
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- mat[i][j] is either 0 or 1
- There is at least one 0 in mat.


Test Case:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

"""

"""
Time Complexity: O(M*N)
Space Complexity: O(M*N) , actually O(3*M*N) O(N x M) for the visited array, distance matrix, and queue space takes up N x M locations at max. 

We are using Breadth First Approach (BFS)

We have used BFS because we are finding for min distance and we do not want to go dfs way as it will go in depth
rather than looking for min this will make unnecessary recursion calls and would not solve our purpose
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        total_rows = len(mat)
        total_cols = len(mat[0])
        queue = []
        is_visited = [[False for c in range(total_cols)] for r in range(total_rows)] 
        result = [[None for _ in range(total_cols)] for _ in range(total_rows)] 

        for r in range(total_rows):
            for c in range(total_cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    is_visited[r][c] = True
        
        def add_adj_element(row, col, steps):
            # handle invalid indexes
            if row < 0 or row >= total_rows or col < 0 or col >= total_cols or is_visited[row][col]:
                return 
            # Mark the current element visited 
            is_visited[row][col] = True    
            queue.append((row, col, steps))
            

        while queue:
            row,col,steps = queue.pop(0)

            result[row][col] = steps

            # add top element
            add_adj_element(row-1, col, steps+1)
            # add right element
            add_adj_element(row, col+1, steps+1)
            # add bottom element
            add_adj_element(row+1, col, steps+1)
            # add left element
            add_adj_element(row, col-1, steps+1)

        return result

            




        














