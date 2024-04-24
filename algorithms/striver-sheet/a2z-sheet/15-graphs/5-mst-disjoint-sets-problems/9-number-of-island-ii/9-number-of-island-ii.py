""" 
Number of Islands II

Problem Link:
https://www.naukri.com/code360/problems/largest-island_840701

Statement
You are given two integers 'n' and 'm', the dimensions of a grid. The coordinates are from (0, 0) to (n - 1, m - 1).
The grid can only have values 0 and 1.
The value is 0 if there is water and 1 if there is land.
An island is a group of ‘1’s such that every ‘1’ has at least another ‘1’ sharing a common edge.
You are given an array 'queries' of size 'q'.
Each element in 'queries' contains two integers 'x' and 'y', referring to the coordinates in the grid.
Initially, the grid is filled with 0, which means only water and no land.
At each query, the value of 'grid' at (x, y) becomes 1, which means it becomes land.
Find out, after each query, the number of islands in the grid.

Constraints:
- 1 <= 'n', 'm' <= 1000
- 1 <= 'q' <= 10 ^ 4
- 0 <= 'x' < 'n'
- 0 <= 'y' < 'm'
- All the (x, y) pairs are unique.

Test Case:
Input: 'n' = 3, 'm' = 4
'queries' = [[1, 1], [1, 2], [2, 3]]

Output: [1, 1, 2]

"""

"""
Approach: Disjoint Sets

Time Complexity: O(Q* 4 * alpha) + O(N*M), n is no of rows, m is no of columns and q is no of online queries, 4*alpha is almost constant time

Space Complexity: O(Q) + O(N*M)


"""
from typing import List

def numberOfIslandII(n: int, m: int, queries: List[List[int]], q: int)-> int:
    # Write your code here.
    rank = [0] * (n*m)
    parent = [i for i in range(n*m)]
    result = []
    
    def get_ultimate_parent(node):
        # base case
        if parent[node] == node:
            return parent[node]
        
        ultimate_par = get_ultimate_parent(parent[node])
        parent[node] = ultimate_par
        return parent[node]

    def union_by_rank(u, v):
        # get ultimate parent of u and v
        ulp_u = get_ultimate_parent(u)
        ulp_v = get_ultimate_parent(v)

        if ulp_u == ulp_v:
            return
        
        if rank[ulp_u] > rank[ulp_v]:
            parent[ulp_v] = ulp_u
        elif rank[ulp_u] < rank[ulp_v]:
            parent[ulp_u] = ulp_v
        # Add first as parent of second and increase rank of parent
        else:
            parent[ulp_v] = ulp_u
            rank[ulp_u] += 1
        
    def union_with_neighbour_node(cur_node, r, c, no_of_islands):
        # top, right, bottom, left
        adj_row_col = [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]
        
        for adj_r_c in adj_row_col:
            row, col = adj_r_c
            # valid row col
            if row >= 0 and row < n and col >= 0 and col < m and adj_matrix[row][col] == 1:
                adj_node = m*row + col
                # compare if both ultimate parent are same then they are already connected if not run
                # the union by rank fn
                if not get_ultimate_parent(cur_node) == get_ultimate_parent(adj_node):
                    no_of_islands -= 1
                    union_by_rank(cur_node, adj_node)\
        
        return no_of_islands


    no_of_islands = 0
    node_set = set()
    adj_matrix = [[0 for _ in range(m)] for _ in range(n)]

    for query in queries:
        # only valid 1 should be considered

        u, v = query
        # update adj matrix
        adj_matrix[u][v] = 1
        no_of_islands += 1

        cur_node = m*u + v
        node_set.add(cur_node)
        no_of_islands = union_with_neighbour_node(cur_node, u, v, no_of_islands)
        
        
        result.append(no_of_islands)
    
    return result