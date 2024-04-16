"""
Shortest Path in DAG

Problem Link:
https://www.naukri.com/code360/problems/shortest-path-in-dag_8381897

Statement
You are given a directed acyclic graph of 'N' vertices(0 to 'N' - 1) and 'M' weighted edges.
Return an array that stores the distance(sum of weights) of the shortest path from vertex 0 to all
vertices, and if it is impossible to reach any vertex, then assign -1 as distance.

For Example:
'N' = 3, 'M' = 3, 'edges' = [0, 1, 2], [1, 2, 3], [0, 2, 6]].

Note:
All the nodes are zero-based.

Constraints:
- 1 <= 'N', 'M' <= 10^5
- 1 <= edge weight <= 10^5
- Time Limit: 1 sec



Test Case:

Sample Input 1:
3 3
2 0 4
0 1 3
2 1 2

Sample Output 1:
0 3 -1

"""

"""

Approach 1: Simple DFS solution 

Time Complexity: O(V+E), in detail O(V) + O(V) + O(E) + O(V+E)
O(V+ E) for dfs call, O(V) for adj_list, dist setup each 

Space Complexity: O(V+E), in detail O(V+E) + O(V) + O(V+E)
O(V+E) for adj_list,  O(V) each for dist , O(V+E) recursion stack for dfs

from  typing import *

def shortestPathInDAG(n: int, m: int, edges: List[List[int]]) -> List[int]:
    adj_list = [[] for _ in range(n)]
    dist = [-1] * n

    for item in edges:
        src_node, dest_node, weight = item
        adj_list[src_node].append((dest_node, weight))
        
    # Note this is DAG so there will be no cycles
    def dfs(cur_node, d):
        if dist[cur_node] == -1 or d < dist[cur_node]:
            dist[cur_node] = d
        
        for adj_node in adj_list[cur_node]:
            dfs(adj_node[0], d + adj_node[1])

    dfs(0, 0)

    return dist

"""


"""
Approach 2: Topo Sort with DFS approach used 
This is better than simple DFS as no of calls are reduced significantly.

Time Complexity: O(V+E)
Space Complexity: O(V+E)
"""
from  typing import *
# topo sort using stack approach
def get_topo_sort_order(n, adj_list):
    stack = []
    visited = [False]*n

    def topo_sort(node):
        if visited[node]:
            return 

        visited[node] = True
        for adj_node in adj_list[node]:
            topo_sort(adj_node[0])
        
        stack.append(node)
    # Note instead of running a for loop over the complete graph nodes
    # we already know from problem that our source node is 0 so we 
    # do not need to find it
    topo_sort(0)
    
    return stack


def shortestPathInDAG(n: int, m: int, edges: List[List[int]]) -> List[int]:
    # creating adjacenty list
    adj_list = [[] for _ in range(n)]
    dist= [-1]*n
    for item in edges:
        src_node, dest_node, weight = item
        adj_list[src_node].append((dest_node, weight))
        
    stack = get_topo_sort_order(n, adj_list)
    
    # setting up the distance 0 for src node, top element of stack returned
    # from a topo sort will be source node of DAG
    dist[stack[-1]] = 0

    while stack:
        cur_node = stack.pop()

        for adj_node in adj_list[cur_node]:
            # distance till cur_node will be dist[cur_node]
            if dist[adj_node[0]] == -1 or dist[cur_node] + adj_node[1] < dist[adj_node[0]]:
                dist[adj_node[0]] = dist[cur_node] + adj_node[1]
            


    return dist
    