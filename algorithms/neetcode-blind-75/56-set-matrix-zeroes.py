from typing import List


"""
Time Complexity: O(m*n)
Space Complexity: O(m+n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Do not return anything, modify matrix in-place instead.
        rows  = set()
        cols = set()

        no_of_rows = len(matrix)
        no_of_cols = len(matrix[0])

        for r in range(no_of_rows):
            for c in range(no_of_cols):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in range(no_of_rows):
            for c in range(no_of_cols):
                if r in rows or c in cols:
                    matrix[r][c] = 0

        return matrix

"""
"""
Approach 2: We have just optmized above approach to use first row and col of the same matrix to
store the 0 reference instead of creating new two arrays row and col

Time Complexity: O(m*n)
Space Complexity: O(1)
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows  = set()
        cols = set()

        no_of_rows = len(matrix)
        no_of_cols = len(matrix[0])
        col_zero = 1

        for r in range(no_of_rows):
            for c in range(no_of_cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0

                    if c == 0:
                        col_zero = 0
                    else:
                        matrix[0][c] = 0

        for r in range(1, no_of_rows):
            for c in range(1, no_of_cols):
                if matrix[r][0] == 0:
                    matrix[r][c] = 0

                if matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for c in range(no_of_cols):
                matrix[0][c] = 0

        if col_zero == 0:
            for r in range(no_of_rows):
                matrix[r][0] = 0

        return matrix
