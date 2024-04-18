"""
Network Delay Time

Problem Link:
https://leetcode.com/problems/network-delay-time/

Statement
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as 
directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time 
it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the
signal. If it is impossible for all the n nodes to receive the signal, return -1.


Constraints:
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

Test Case:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
"""


"""
Approach: Using Dijstras Algorithm (as it is weighted graph)

Time Complexity: O(E log n), E is size of times array n is no of nodes, in detail O(n) + O(n) + O(E) len of times array , O(E log V) for dijstras algorithm
Space Complexity: O(n + E) , n is no of vertices and E is edges
"""
from heapq import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # setting up adj list
        adj_list = [[] for _ in range(n+1)]
        # Note: we are using dist instead of time, dist here represents time 
        dist = [float("inf") for _ in range(n+1)] 
        
        for time in times:
            s, d, w = time
            adj_list[s].append((d, w))
        
        priority_queue = []
        heappush(priority_queue, (0, k)) # (dist, cur_node)
        dist[k] = 0

        while priority_queue:
            dist_to_cur_node, cur_node = heappop(priority_queue)
            
            for adj_node_details in adj_list[cur_node]:
                adj_node, adj_node_edge_weight = adj_node_details

                if dist_to_cur_node + adj_node_edge_weight < dist[adj_node]:
                    dist[adj_node] = dist_to_cur_node + adj_node_edge_weight 
                    heappush(priority_queue, (dist[adj_node], adj_node))
        
        max_dist = -1
        print(adj_list)
        print(dist)
        for i in range(1, n+1, 1):
            if dist[i] > max_dist:
                max_dist = dist[i]

       
        return max_dist if not max_dist == float("inf") else -1





        