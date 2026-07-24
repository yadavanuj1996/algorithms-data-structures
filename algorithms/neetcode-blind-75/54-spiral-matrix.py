"""
TC: O(m * n)
SC: O(m * n)
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        no_of_rows = len(matrix)
        no_of_cols = len(matrix[0])
        res = []
        next_dir = {
            "right": "bottom",
            "bottom": "left",
            "left": "top",
            "top": "right",
        }
        visited = [[False for _ in range(no_of_cols)] for _ in range(no_of_rows)]

        def move_spiral_path(r, c, path):
            if r < 0 or r >= no_of_rows or c < 0 or c >= no_of_cols or visited[r][c]:
                return

            visited[r][c] = True
            res.append(matrix[r][c])

            if path == "right":
                if c+1 >= no_of_cols or visited[r][c+1]:
                    next_row = r+1
                    next_col = c
                    next_path = next_dir[path]
                else:
                    next_row = r
                    next_col = c+1
                    next_path = path
            elif path == "bottom":
                if r+1 >= no_of_rows or visited[r+1][c]:
                    next_row = r
                    next_col = c-1
                    next_path = next_dir[path]
                else:
                    next_row = r+1
                    next_col = c
                    next_path = path
            elif path == "left":
                if c-1 < 0 or visited[r][c-1]:
                    next_row = r-1
                    next_col = c
                    next_path = next_dir[path]
                else:
                    next_row = r
                    next_col = c-1
                    next_path = path
            elif path == "top":
                if r-1 < 0 or visited[r-1][c]:
                    next_row = r
                    next_col = c+1
                    next_path = next_dir[path]
                else:
                    next_row = r-1
                    next_col = c
                    next_path = path

            move_spiral_path(next_row, next_col, next_path)

        move_spiral_path(0, 0, "right")
        return res
