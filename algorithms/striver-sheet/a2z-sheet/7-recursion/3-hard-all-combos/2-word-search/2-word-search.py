"""
Word Search

Problem Link:
https://leetcode.com/problems/word-search/

Statement
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
or vertically neighboring. The same letter cell may not be used more than once.

Constraints:
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.


Test Case:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""

"""
Time complexity: O(N* M * 4^W), N is no of rows, M is no of columns and W is length of word
Space complexity: O(W + N * M)
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        col_max = len(board[0])   # row
        row_max = len(board)      # col  
        word_len = len(word)
        visited = [[False for _ in range(col_max)] for _ in range(row_max)]  

        def find_word(row, col, cur_word_ind):
            if cur_word_ind == word_len:
                return True

            if row < 0 or col < 0 or row >= row_max or col >= col_max or visited[row][col] or word[cur_word_ind] != board[row][col]:
                return False
  
            visited[row][col] = True
            #print(cur_seq, visited)

            # top 
            top = find_word(row-1, col, cur_word_ind+1)
            # right
            right = find_word(row, col+1,  cur_word_ind+1)
            # bottom
            bottom = find_word(row+1, col,  cur_word_ind+1)
            # left
            left = find_word(row, col-1,  cur_word_ind+1)

            visited[row][col] = False

            return top or right or bottom or left
        
        for j in range(col_max):
            for i in range(row_max):
                if board[i][j] == word[0]:
                    if find_word(i, j, 0):
                        return True
                         
        return False
        