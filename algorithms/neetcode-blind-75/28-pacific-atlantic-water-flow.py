"""
TC: O(m * n)
SC: O(m * n)

Reverse-flow DFS. Instead of asking "can this cell reach both oceans", start
from each ocean's border cells and DFS inward, moving to neighbours with height
>= current (water flows uphill in reverse). Cells reachable from both oceans are
the answer.
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        no_of_rows = len(heights)
        no_of_columns = len(heights[0])

        pacific_ocean_visit = set()
        atlantic_ocean_visit = set()
        result = []

        def dfs(cur_row, cur_col, reachable):
            # if we are getting to this node that means it is visitable/ reachable
            reachable.add((cur_row, cur_col))

            # top, right, bottom, left
            for (x, y) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row = cur_row+x
                new_col = cur_col+y

                if new_row < 0 or new_col < 0 or new_row >= no_of_rows or new_col >= no_of_columns:
                    continue

                if (new_row, new_col) in reachable:
                    continue

                if heights[new_row][new_col] < heights[cur_row][cur_col]:
                    continue

                dfs(new_row, new_col, reachable)


        for r in range(no_of_rows):
            dfs(r, 0, pacific_ocean_visit)
            dfs(r, no_of_columns-1, atlantic_ocean_visit)

        for c in range(no_of_columns):
            dfs(0, c, pacific_ocean_visit)
            dfs(no_of_rows-1, c, atlantic_ocean_visit)

        for r in range(no_of_rows):
            for c in range(no_of_columns):
                if (r, c) in pacific_ocean_visit and (r, c) in atlantic_ocean_visit:
                    result.append([r, c])

        return result
