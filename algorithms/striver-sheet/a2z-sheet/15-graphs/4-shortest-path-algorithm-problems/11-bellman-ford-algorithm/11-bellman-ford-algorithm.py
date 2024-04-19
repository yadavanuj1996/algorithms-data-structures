"""
Bellman Ford

Problem Link:
https://www.naukri.com/code360/problems/bellman-ford_2041977

Statement
You have been given a directed weighted graph of ‘N’ vertices labeled from 1 to 'N' and ‘M’ edges. Each edge 
connecting two nodes 'u' and 'v' has a weight 'w' denoting the distance between them.

Your task is to calculate the shortest distance of all vertices from the source vertex 'src'.

Note:
If there is no path between 'src' and 'ith' vertex, the value at 'ith' index in the answer array will be 10^8.

Note :

It's guaranteed that the graph doesn't contain self-loops and multiple edges. Also, the graph does not contain 
negative weight cycles.

Constraints:
- 1 <= N <= 50
- 1 <= M <= 300
- 1 <= src <= N
- 1 <= u,v <= N
- -10^5 <= w <= 10^5

Time Limit: 1 sec

Test Case:

Sample Input 1 :
4 4 1
1 2 4
1 3 3
2 4 7 
3 4 -2

Sample Output 1 :
0 4 3 1
"""

"""
Intuition & Approach:
In this problem we need to find shortest distance of weighted graph with negative weights
so this can be solved by Bellman Ford Algorithm.

Also, the graph does not contain negative weight cycles as it is mentioned in the problem
so we do not need to check for -ve cycles.

Time Complexity: O(n) + O(n*m), n is no of vertices & m is no of edges. O(n*m) for looping over each itertation all edges and O(n) for populating dist array
Space Complexity: O(n), for dist array
"""
from collections import *
from math import *

def bellmonFord(n, m, src, edges):
    dist = [10**8] * (n+1)
    # for source node dist is 0
    dist[src] = 0
    # for n-1 relaxation 
    for i in range(n-1):
        # sequentially relaxing each edge
        for edge in edges:
            s_node, d_node, weight = edge
            if dist[s_node] + weight < dist[d_node]:
                dist[d_node] = dist[s_node] + weight

    return dist
