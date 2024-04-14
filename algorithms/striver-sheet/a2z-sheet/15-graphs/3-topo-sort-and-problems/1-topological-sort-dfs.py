"""
Topological Sort

Problem Link:
https://www.codingninjas.com/studio/problems/982938?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTabValue=PROBLEM

Statement
A Directed Acyclic Graph (DAG) is a directed graph that contains no cycles.

Topological Sorting of DAG is a linear ordering of vertices such that for every directed edge from vertex ‘u’ to vertex ‘v’, vertex ‘u’ comes before ‘v’ in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

Given a DAG consisting of ‘V’ vertices and ‘E’ edges, you need to find out any topological sorting of this DAG. Return an array of size ‘V’ representing the topological sort of the vertices of the given DAG.


Constraints:
- 1 <= T <= 50
- 1 <= V <= 10^4
- 0 <= E <= 10^4
- 0 <= u, v < V 


Test Case:

Input: 
2
2 1
1 0
3 2
0 1
0 2

Output:  
1 0
0 2 1

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