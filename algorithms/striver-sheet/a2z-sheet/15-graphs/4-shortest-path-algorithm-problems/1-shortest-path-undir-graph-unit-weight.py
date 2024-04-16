"""
Single Source Shortest Path

Problem Link:
https://www.naukri.com/code360/problems/single-source-shortest-path_8416371

Statement
You are given an undirected graph with 'N' nodes and 'M' edges. The weight of each edge in the graph
is one unit.
Given a source vertex 'src', you must return an array 'answer' of length 'N', where 'answer[i]' is 
the shortest path length between the source vertex 'src' and 'i'th vertex.

Note:
All the nodes are zero-based.

Constraints:
- 1 <= N, M <= 10^2
- 0 <= src, edges[0], edges[0] <= N-1
- Time Limit: 1 sec



Test Case:

Sample Input 1:
4 3
0 1
0 3
2 3
0
Sample Output 1:
0 1 2 1

"""

"""
Time Complexity: O(V+E)
Space Complexity: O(V+E)

"""
from typing import List

def shortestPath(n:int, edges: List[List[int]], src:int ) -> List[int]:
    # Write your code here
    adj_list_input = [[] for _ in range(n)]
    for item in edges:
        adj_list_input[item[0]].append(item[1])
        adj_list_input[item[1]].append(item[0])
    
    # Approach using BFS
    queue = []
    visited = [False] * n
    queue.append((src, 0))
    result = [-1] * n

    while queue:
        cur_node, dis = queue.pop(0)
        
        if visited[cur_node]:
            continue
        
        visited[cur_node] = True
        result[cur_node] = dis
        
        for adj_node in adj_list_input[cur_node]:
            queue.append((adj_node, dis+1))
    
    return result
        

