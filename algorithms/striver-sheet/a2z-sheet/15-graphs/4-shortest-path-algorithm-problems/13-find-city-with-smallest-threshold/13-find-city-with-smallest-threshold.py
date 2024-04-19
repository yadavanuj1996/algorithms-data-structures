""" 
Find the City With the Smallest Number of Neighbors at a Threshold Distance

Problem Link:
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

Statement
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents
a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at 
most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that
path.


Note :
It's guaranteed that the graph doesn't contain self-loops and multiple edges. Also, the graph does not contain 
negative weight cycles.


Constraints:
- 2 <= n <= 100
- 1 <= edges.length <= n * (n - 1) / 2
- edges[i].length == 3
- 0 <= from[i] < to[i] < n
- 1 <= weight[i], distanceThreshold <= 10^4
- All pairs (from[i], to[i]) are distinct.

Test Case:

Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3

Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
"""

"""
Approach: Using Floyd Warshal Algorithm
Time Complexity: O(V^3) , V is no of vertices
Space Complexity: O(V^2)
"""
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Step 1: Create a dist_matrix 2d array with unreachable values infinity
        dist_matrix = [[float("inf") for _ in range(n)] for _ in range(n)]

        # Step 2: set all nodes that point to themselves as 0, as reaching itself takes 0 
        # distance and no self loop is possible
        for s_node in range(n):
                for d_node in range(n):
                    if s_node == d_node:
                        dist_matrix[s_node][d_node] = 0
                        
        
        # Step 3: set values if edges directly connect two nodes, setup dist_matrix values 
        # on the basis of edges
        for edge in edges:
            s_node, d_node, weight = edge
            # Note: it is undirected hence we are updating for s -> d and d -> s dist values
            dist_matrix[s_node][d_node] = weight
            dist_matrix[d_node][s_node] = weight

        # Step 4: travel from each node to all other nodes using a via node logic
        for via_node in range(n):
            for s_node in range(n):
                for d_node in range(n):
                    dist_matrix[s_node][d_node] = min(dist_matrix[s_node][d_node], dist_matrix[s_node][via_node] + dist_matrix[via_node][d_node])

        city_node, adj_city_count = -1, float("inf")
        
        for s_node in range(n):

            count_of_ajd_cities = 0
            for d_node in range(n):
                count_of_ajd_cities += 1 if dist_matrix[s_node][d_node] <= distanceThreshold else 0
                
            
            if count_of_ajd_cities <= adj_city_count:
                city_node, adj_city_count = s_node, count_of_ajd_cities
                
        return city_node
                    

        
        

