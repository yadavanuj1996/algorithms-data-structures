"""
Topological Sort

Problem Link:
https://www.geeksforgeeks.org/problems/topological-sort/1

Statement
Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.

Constraints:
- 2 ≤ V ≤ 10^4
- 1 ≤ E ≤ (N*(N-1))/2


Test Case:
Input:  (In form of 2d list in python) (Valid DAGs will be provided)

3 4 (Edges, Vertices)
3 0
1 0
2 0

adj = [ [], [0], [0], [0] ]

Output:  
return an list with topo sorted elements
[1,2,3,0]

"""

"""
Time complexity: 
Space Complexity:
"""

from os import *
from sys import *
from collections import deque
from math import *

def topologicalSort(adj, v, e):
    node_graph = [ [] for i in range(v) ]
    for item in adj:
        # None check for input issue in coding ninjas
        if item[0] is not None:
            node_graph[item[0]].append(item[1])

    
    visited_nodes = [0] * v
    # stack implementation of deque
    dq = deque()

    def topoSort(node):
        if visited_nodes[node]:
            return 

        visited_nodes[node] = 1
        for adj_node in node_graph[node]:
            topoSort(adj_node)

        dq.append(node)
    
    for cur_node in range(v):
        topoSort(cur_node)

    
    res = []
    
    while dq:
        val = dq.pop()
        res.append(val)
    
    return res