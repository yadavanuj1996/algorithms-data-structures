"""
BFS in Graph

Problem Link:
https://www.codingninjas.com/studio/problems/bfs-in-graph_973002?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&count=25&page=2&search=&sort_entity=order&sort_order=ASC&leftPanelTabValue=PROBLEM

Statement
Given an adjacency list representation of a directed graph with ‘n’ vertices and ‘m’ edges. Your task is to return a list consisting of Breadth-First Traversal (BFS) starting from vertex 0.

In this traversal, one can move from vertex 'u' to vertex 'v' only if there is an edge from 'u' to 'v'. The BFS traversal should include all nodes directly or indirectly connected to vertex 0.

Constraints:
- 1 <= 'n', 'm' <= 10^4 (Where 'n' is the number of vertices and 'm' is the number of edges)



Test Case:

Input:  (In form of 2D list)
4 4
0 1
0 2
1 2
0 3

Output:  (In form of list)
0 1 2 3

"""

"""
Time complexity: O(N) + O(2E) , n is nodes & e is no of edges 
Space Complexity: O(N)
"""

from typing import List
from collections import deque

def bfsTraversal(n: int, adj: List[List[int]]) -> List[int]:
    dq = deque()
    visited_nodes = [0] * n
    res = []
    dq.append(0)
    
    while dq:
        node = dq.popleft()
        if not visited_nodes[node]:
            visited_nodes[node] = 1
            res.append(node)
            for adjacent_node in adj[node]:
                dq.append(adjacent_node)
    
    return res


adjList = [[1, 2, 3], [4, 7], [5], [6], [], [], [], []]  # [[1,2, 3], [2], [], []]
n = len(adjList)
print(bfsTraversal(n, adjList))