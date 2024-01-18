"""

N-Queens

Problem Link:
https://leetcode.com/problems/valid-parentheses/

Statement
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens 
attack each other. Given an integer n, return all distinct solutions to the n-queens puzzle. You may return
the answer in any order. Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.


Constraints:
- 1 <= n <= 9

Test Case:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

"""
# Time Complexity: O(N!)
# Space Complexity: O(N^2)

"""
Solution 1

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [ [ "." for _ in range(n)] for _ in range(n)]
        result = []
        def solveNQueensProblem(row, col, grid):
            if col == n:
                val= []
                for i in range(len(grid)):
                    s=""
                    for j in range(len(grid[0])):
                        s += grid[i][j]
                    val.append(s)
                
                result.append(copy.deepcopy(val))
                return
            
            if row == n:
                return 
            
            #print(row, col, fn)
            if can_queen_be_placed(row, col, grid):
                grid[row][col] = "Q"
                

                solveNQueensProblem(0, col+1, grid)
                grid[row][col] = "."
                solveNQueensProblem(row+1, col, grid)
            else:
                solveNQueensProblem(row+1, col, grid)
        
        def can_queen_be_placed(row, col, grid):
            #print(row,col)
            if row < 0 or col < 0 or row >= n or col >= n:
                return True
            
            if grid[row][col] == "Q":
                return False
            # left check 
            left_path = True
            temp_col = col
            while temp_col >= 0:
                if grid[row][temp_col] == "Q":
                    left_path = False
                    break

                temp_col -= 1
            
             
            # left up check 
            left_up_path = True
            temp_row = row
            temp_col = col
            while temp_row >= 0 and temp_col >= 0:
                if grid[temp_row][temp_col] == "Q":
                    left_up_path = False
                    break

                temp_row -= 1
                temp_col -= 1


            # left down check 
            left_down_path = True
            temp_row = row
            temp_col = col
            while temp_row < n and temp_col >= 0:
                if grid[temp_row][temp_col] == "Q":
                    left_down_path = False
                    break

                temp_row += 1
                temp_col -= 1

            return left_path and left_up_path and left_down_path
        
        solveNQueensProblem(0, 0, grid)
        return result


"""









        