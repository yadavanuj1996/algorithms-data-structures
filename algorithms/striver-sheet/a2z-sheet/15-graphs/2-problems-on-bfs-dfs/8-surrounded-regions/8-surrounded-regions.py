"""
Surrounded Regions

Problem Link:
https://leetcode.com/problems/surrounded-regions/

Statement
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 
'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Constraints:
- m == board.length
- n == board[i].length
- 1 <= m, n <= 200
- board[i][j] is 'X' or 'O'.


Test Case:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

"""

"""
Time Complexity: O(N*M),  actually  O(N) + O(M) + O(N * M * 4) for two loops also O(N*M) recursion calls (Note: whether the first row or last row calls dfs max it can be called is N*M times.). Also 4 times is because each dfs fn will call it 4 times top, left, right, bottom
Space Complexity: O(N*M) ,  recursion stack space
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        total_rows = len(board)
        total_cols = len(board[0])
        
        def mark_boundary_o(row, col):
            if row < 0 or row >= total_rows or col < 0 or col >= total_cols or board[row][col] is None or \
            board[row][col] == "X":
                return 

            board[row][col] = None

            # top 
            mark_boundary_o(row-1, col)
            # right
            mark_boundary_o(row, col+1)
            # bottom
            mark_boundary_o(row+1, col)
            # left
            mark_boundary_o(row, col-1)
            

        # first row and last row
        for c in range(total_cols):
            if board[0][c] == "O":
                mark_boundary_o(0, c)
            
            if board[total_rows-1][c] == "O":
                mark_boundary_o(total_rows-1, c)
        
        # first col and last col
        for r in range(total_rows):
            if board[r][0] == "O":
                mark_boundary_o(r, 0)
            
            if board[r][total_cols-1] == "O":
                mark_boundary_o(r, total_cols-1)
        
        for r in range(total_rows):
            for c in range(total_cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif not board[r][c]:
                    board[r][c] = "O"
        

