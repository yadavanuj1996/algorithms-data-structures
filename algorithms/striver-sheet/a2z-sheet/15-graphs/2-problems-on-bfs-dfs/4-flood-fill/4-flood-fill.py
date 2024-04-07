"""
Flood Fill

Problem Link:
https://leetcode.com/problems/flood-fill/

Statement
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the 
image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting 
from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the 
starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Constraints:
- m == image.length
- n == image[i].length
- 1 <= m, n <= 50
- 0 <= image[i][j], color < 216
- 0 <= sr < m
- 0 <= sc < n


Test Case:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

"""

"""
Time Complexity: O(4 * N * M), in worst case we will call fill_color (dfs function) 4 times for each node
Space Complexity: O(N*M), recursion stack space
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        total_rows = len(image)
        total_cols = len(image[0])

        # DFS Approach without is visited array approach
        def fill_color(row_no, col_no, prev_color=None):
            if row_no < 0 or row_no >= total_rows or col_no < 0 or \
                col_no >= total_cols:
                return 

            if prev_color is not None and not prev_color == image[row_no][col_no] or\
                image[row_no][col_no] == color:
                return 
            
            old_color = image[row_no][col_no]
            image[row_no][col_no] = color

            # top 
            fill_color(row_no-1, col_no, old_color)
            # right
            fill_color(row_no, col_no+1, old_color)
            # bottom
            fill_color(row_no+1, col_no, old_color)
            # left 
            fill_color(row_no, col_no-1, old_color)
  

        fill_color(sr, sc, None)

        return image