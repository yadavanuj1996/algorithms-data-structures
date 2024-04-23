""" 
Most Stones Removed with Same Row or Column

Problem Link:
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

Statement
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been 
removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the
largest possible number of stones that can be removed.

Constraints:
- 1 <= stones.length <= 1000
- 0 <= xi, yi <= 10^4
- No two stones are at the same coordinate point.

Test Case:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.


"""

"""
Approach 1: Disjoint Sets

Time Complexity: O(N), where N = total no. of stones. Here we have just traversed the given stones array several times. And inside those loops, every operation is apparently taking constant time. So, the time complexity is only the time of traversal of the array.

Space Complexity: O(2* (max row index + max column index)) for the parent and size array inside the Disjoint Set data structure.


"""
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        max_r, max_c = 0, 0
        n = len(stones)

        for edge in stones:
            r, c = edge
            max_r = max(max_r, r)
            max_c = max(max_c, c)
        
        total_nodes = (max_r+1) + (max_c+1)

        rank = [0] * total_nodes
        parent = [i for i in range(total_nodes)]

        def get_ultimate_parent(node):
            # base case
            if node == parent[node]:
                return node
            
            ultimate_par = get_ultimate_parent(parent[node])
            parent[node] = ultimate_par
            return parent[node]

        def union_by_rank(u, v):
            ulp_u = get_ultimate_parent(u)
            ulp_v = get_ultimate_parent(v)
        
            if ulp_u == ulp_v:
                return
            
            if rank[ulp_u] < rank[ulp_v]:
                parent[ulp_u] = ulp_v
            elif rank[ulp_u] > rank[ulp_v]:
                parent[ulp_v] = ulp_u
            # make any one parent and increase rank of other by 1
            else:
                parent[ulp_v] = ulp_u
                rank[ulp_u] += 1
        
        node_set = set()
        for edge in stones:
            u, v = edge
            v = (max_r+1) + v
            # call union by rank and connect all the nodes in disjoint set
            union_by_rank(u, v)
            # only add the nodes that have stones on it
            node_set.add(u)
            node_set.add(v)

        
        no_of_comp = 0
        for node in node_set:
            if node == parent[node]:
                no_of_comp += 1

        return n - no_of_comp

        