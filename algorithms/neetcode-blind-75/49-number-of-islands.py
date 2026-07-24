"""
TC: O(m * n)
SC: O(m * n)
"""
from typing import List


class Solution:


    def numIslands(self, grid: List[List[str]]) -> int:
        total_rows = len(grid)
        total_columns = len(grid[0])
        visited_nodes = []
        for i in range(total_rows):
            temp_arr = []
            for j in range(total_columns):
                temp_arr.append(0)
            visited_nodes.append(temp_arr)


        total_dist_comp = 0

        def islandHop(i,j):

            if not (i < total_rows and j < total_columns and i >= 0 and j >= 0):
                return False
            if grid[i][j] == "0" or visited_nodes[i][j]:
                return False

            if not visited_nodes[i][j] and grid[i][j] == "1":
                visited_nodes[i][j] = 1
                islandHop(i+1,j)
                islandHop(i-1,j)
                islandHop(i,j+1)
                islandHop(i,j-1)

            return True

        for row_index in range(total_rows):
            for column_index in range(total_columns):
                if not visited_nodes[row_index][column_index]:
                    if islandHop(row_index, column_index):
                        print(row_index, column_index)
                        total_dist_comp += 1


        return total_dist_comp
