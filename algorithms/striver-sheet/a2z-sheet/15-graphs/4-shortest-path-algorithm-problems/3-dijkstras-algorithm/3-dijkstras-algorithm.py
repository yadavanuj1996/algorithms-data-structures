"""
Dijkstra's shortest path

Problem Link:
https://www.naukri.com/code360/problems/dijkstra's-shortest-path_985358

Statement
You have been given an undirected, connected graph of ‘V’ vertices (labelled from 0 to V-1) and ‘E’ 
edges. Each edge connecting two nodes 'u' and 'v' has a weight denoting the distance between them.

Your task is to find the shortest path distance from the source node 'S' to all the vertices. 
You have to return a list of integers denoting the shortest distance between each vertex and source
vertex 'S'.

Note:
1. There are no self-loops(an edge connecting the vertex to itself) in the given graph.
2. There are no parallel edges i.e no two vertices are directly connected by more than 1 edge.

Note:
All the nodes are zero-based.

Constraints:
- 1 <= 'V' <= 10^5
- 1 <= 'E' <= 10^5
- 1 <= distance between vertices <= 10^5


Test Case:

Sample Input 1
5 7 0
0 1 7
0 2 1
0 3 2
1 2 3
1 3 5 
1 4 1
3 4 7

Sample Output 1
0 4 1 2 5

"""

"""
Dijstras Algorithm implementation for an weighted undirected graph

Time Complexity: O(E log V), rote learn for now re-read the derivation later
Space Complexity: O(V + E)
"""
from typing import List
from heapq import *

def dijkstra(edge: List[List[int]], vertices: int, edges: int, source: int):
    # Write your code here.
    # edge' contains {u, v, distance} vectors.
    # Adding to adj list input
    adj_list = [[] for _ in range(vertices)]
    
    for item in edge:
        src_node = item[0]
        dest_node = item[1]
        weight = item[2]
        # As it is undirected we need to add both side
        adj_list[src_node].append((dest_node, weight))
        adj_list[dest_node].append((src_node, weight))

    # setting up dist and priority queue
    dist = [float("inf")] * vertices
    priority_queue = []             # Add (dist, node)
    
    # setting up source node distance and adding it to priority queue
    dist[source] = 0
    heappush(priority_queue, (dist[source], source))
    
    while priority_queue:
        # this will pop the item that will have min distance
        cur_path_dis, cur_node = heappop(priority_queue)
        
        for adj_node_detail in adj_list[cur_node]:
            adj_node = adj_node_detail[0]
            adj_node_dist = adj_node_detail[1]
            
            if cur_path_dis + adj_node_dist < dist[adj_node]:
                dist[adj_node] = cur_path_dis + adj_node_dist
                
                heappush(priority_queue, (dist[adj_node], adj_node))
                
    return dist