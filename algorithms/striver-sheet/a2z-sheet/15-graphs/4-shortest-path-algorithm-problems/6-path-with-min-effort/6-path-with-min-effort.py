"""
Path With Minimum Effort

Problem Link:
https://leetcode.com/problems/path-with-minimum-effort/

Statement
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, 
where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), 
and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, 
left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



Constraints:
- rows == heights.length
- columns == heights[i].length
- 1 <= rows, columns <= 100
- 1 <= heights[i][j] <= 10^6


Test Case:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
"""

"""
Approach: Using Dijstras Algorithm, also it's about finding min effort so we know we will use BFS with queue DS
but on closer look we note there are different weights so we conclude we will use dijstras algorithm.

Time Complexity: O( 4*N*M * log (N*M) ), TC of dijstras algorithm is O(E log V), total vertices-> N*M, also 4*N*M as we are adding all 4 adj nodes in the pq
Space Complexity: O(N*M), PQ may contain all the elements
"""
from heapq import *

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dist = float("inf")
        no_of_rows = len(heights)
        no_of_cols = len(heights[0])
        visited = [[False for _ in range(no_of_cols)] for _ in range(no_of_rows)]
        dist = [[float("inf") for _ in range(no_of_cols)] for _ in range(no_of_rows)]
        priority_queue = []
        heappush(priority_queue, (0, (0, 0)))

        while priority_queue:
            abs_diff, (row, col) = heappop(priority_queue)

            dir = [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]

            for item in dir:
                r, c = item

                if not (r < 0 or r >= no_of_rows or c < 0 or c >= no_of_cols):
                    next_abs_diff = (max(abs_diff ,abs(heights[row][col]-heights[r][c])))
                    if next_abs_diff < dist[r][c]:
                        dist[r][c] = next_abs_diff
                        heappush(priority_queue, (next_abs_diff, (r,c)))

        return dist[no_of_rows-1][no_of_cols-1] if not dist[no_of_rows-1][no_of_cols-1] == float("inf") else 0

