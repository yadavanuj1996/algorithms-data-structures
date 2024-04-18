"""
Cheapest Flights Within K Stops

Problem Link:
https://leetcode.com/problems/cheapest-flights-within-k-stops/

Statement
There are n cities connected by some number of flights. You are given an array flights where 
flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city to[i] with cost price[i].

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.


Constraints:
- 1 <= n <= 100
- 0 <= flights.length <= (n * (n - 1) / 2)
f- lights[i].length == 3
- 0 <= from[i], to[i] < n
- from[i] != to[i]
- 1 <= price[i] <= 104
- There will not be any multiple flights between two cities.
- 0 <= src, dst, k < n
- src != dst


Test Case:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700

Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

"""


"""
Approach: Using Dijstras Algorithm (as it is weighted graph)

Also, a point to note here is that do we really need a priority queue for carrying out the algorithm? 
The answer for that is No because when we are storing everything in terms of a number of stops, the 
stops are increasing monotonically which means that the number of sops is increasing by 1 and when we 
pop an element out of the queue, we are always popping the element with a lesser number of stops first.
Replacing the priority queue with a simple queue will let us eliminate an extra log(N) of the complexity 
of insertion-deletion in a priority queue which would in turn make our algorithm a lot faster.

Time Complexity: O(E) here E is size of flights array, dijstras has O(E log V) here we have not used PQ so log V is removes only O(Edges)
Space Complexity: O(E+V) , adj_list, queue and O(n) for dist array
"""
from heapq import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # create an adj list
        adj_list = [[] for _ in range(n)]
        dist = [float("inf")] * n
        for flight in flights:
            s, d, weight = flight
            adj_list[s].append((d, weight))

        queue = []
        queue.append((0, src, 0)) # no of stops, node, dist

        while queue:
            no_of_stops, cur_node, dist_to_node = queue.pop(0)
            if no_of_stops > k:
                break
            
            for adj_node_details in adj_list[cur_node]:
                adj_node, edge_weight = adj_node_details

                if dist_to_node + edge_weight < dist[adj_node]:
                    dist[adj_node] = dist_to_node + edge_weight
                    queue.append((no_of_stops+1, adj_node, dist[adj_node]))
        
        return dist[dst] if not dist[dst] == float("inf") else -1