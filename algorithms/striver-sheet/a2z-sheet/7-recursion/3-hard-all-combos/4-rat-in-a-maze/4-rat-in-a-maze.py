
"""
Rat In a Maze

Problem Link:
https://www.codingninjas.com/studio/problems/rat-in-a-maze-_8842357

Statement
You are given a N*N maze with a rat placed at 'mat[0][0]'. Find all paths that rat can follow to reach
its destination i.e. mat[N-1][N-1]. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left),
'R' (right).

In the given maze, each cell can have a value of either 0 or 1. Cells with a value of 0 are considered blocked,
which means the rat cannot enter or traverse through them. On the other hand, cells with a value of 1 are open,
indicating that the rat is allowed to enter and move through those cells.

Example:
mat:{{1, 0, 0, 0},
     {1, 1, 0, 1}, 
     {1, 1, 0, 0},
     {0, 1, 1, 1}}

All possible paths are:
DDRDRR (in red)
DRDDRR (in green)


Constraints:
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.


Test Case:

Sample Input 1 :
3
1 1 1
1 0 1
1 1 1
Sample Output 1 :

DDRR
RRDD

"""

"""
Time Complexity: O(4^(m*n)), because on every cell we need to try 4 different directions.
Space Complexity:  O(m*n), Maximum Depth of the recursion tree(auxiliary space).
"""

from typing import List

def ratMaze(matrix: List[List[int]]) -> List[str]:
    n = len(matrix)
    result = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    # Write your code here.
    def rat_maze(row, col, cur_seq):
        if row < 0 or col < 0 or row >= n or col >= n or not matrix[row][col] or visited[row][col]:
            return
        
        if row == n-1 and col == n-1:
            result.append(cur_seq)
            return
        
        visited[row][col] = True
        # Note : we did not added and removed character in cur_seq 
        # becuase we have directly passed in the fn still we are 
        # doing the backtracking
        
        # top
        rat_maze(row-1, col, cur_seq+"U")
        # right
        rat_maze(row, col+1, cur_seq+"R")
        # bottom
        rat_maze(row+1, col, cur_seq+"D")
        # left
        rat_maze(row, col-1, cur_seq+"L")

        visited[row][col] = False

    rat_maze(0, 0, "")

    return result
