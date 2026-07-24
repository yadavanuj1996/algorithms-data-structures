"""
TC: O(m * n * 4^L)
SC: O(L) recursion (+ O(m*n) visited)
"""
from typing import List


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
