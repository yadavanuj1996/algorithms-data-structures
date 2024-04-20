""" 
Minimum Spanning Tree

Problem Link:
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

Statement
You are given an undirected, connected and weighted graph G(V, E), consisting of V number of vertices (numbered
from 0 to V-1) and E number of edges.

Find and print the total weight of the Minimum Spanning Tree (MST) using Kruskal's algorithm.
(NOTE: the original problem had krushkal but for practice we have solved it using prims algorithm)

By definition, a minimum weight spanning tree is a subset of the edges of a connected, edge-weighted undirected 
graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.



Constraints:
- 2 <= V <= 10^5
- 1 <= E <= 3 * 10^5
- 0 <= X < N
- 0 <= Y < N
- 1 <= W <= 10^4

Test Case:

Sample Input 1 :
4 4
0 1 3
0 3 5
1 2 1
2 3 8
Sample Output 1 :
9
Explanation for Sample Input 1:
The edge (2,3) having weight 8 will be excluded from the MST. The total weight of the MST then will be 1 + 3 + 5 = 9.
"""

"""
Approach: Using Prims Algorithm
Time Complexity: O(E*logE) + O(E*logE)~ O(E*logE), where E = no. of given edges.
The maximum size of the priority queue can be E so after at most E iterations the priority queue will be empty and the loop will end. Inside the loop, there is a pop operation that will take logE time. This will result in the first O(E*logE) time complexity. Now, inside that loop, for every node, we need to traverse all its adjacent nodes where the number of nodes can be at most E. If we find any node unvisited, we will perform a push operation and for that, we need a logE time complexity. So this will result in the second O(E*logE). 

Space Complexity: O(E) + O(V), where E = no. of edges and V = no. of vertices. O(E) occurs due to the size of the priority queue and O(V) due to the visited array. If we wish to get the mst, we need an extra O(V-1) space to store the edges of the most.
"""
# Edge class for storing the Edges of thee graph
class Edge:
    
    def __init__(self, start, end, weight) :

        self.start = start
        self.end = end
        self.weigth = weight

from heapq import *

def minimumSpanningTree(edges, V, E):
    # your code goes here
    visited = [False] * V
    priority_queue = []
    mst_edges = []
    mst_weight = 0
    # Create adj list
    adj_list = [[] for _ in range(V)]
    for edge in edges:
        s_node = edge.start
        d_node = edge.end
        weight =  edge.weigth 
        
        adj_list[s_node].append((d_node, weight))
        adj_list[d_node].append((s_node, weight))

	

    heappush(priority_queue, (0, 0, -1)) # (dist, cur_node, parent_node)
    
    while priority_queue:
        edge_weight, cur_node, parent_node = heappop(priority_queue)
        if visited[cur_node]:
            continue
        
        visited[cur_node] = True

        if not parent_node == -1:
            mst_edges.append((parent_node, cur_node))
            mst_weight += edge_weight
        
        for adj_node_details in adj_list[cur_node]:
            adj_node, adj_node_weight = adj_node_details
            # we are checking again to not add extra edges in PQ thus improving time complexity
            if not visited[adj_node]:
                heappush(priority_queue, (adj_node_weight, adj_node, cur_node))




    return mst_weight

