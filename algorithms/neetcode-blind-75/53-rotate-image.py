"""
Time Complexity: O(m*n)
Space Complexity: O(1)

Intuition: If we observe that rotating a arrahy by 90 degree means transposing the matrix
and then reversing the rows
1 2
3 4

Transpose:
1 3
2 4
Reverse rows:
3 1
4 2
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        no_of_rows = len(matrix)
        no_of_cols = len(matrix[0])

        # Transpose the matrix
        for r in range(no_of_rows):
            for c in range(r):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # reverse each row of matrix to get the answer
        for r in range(no_of_rows):
            matrix[r].reverse()
