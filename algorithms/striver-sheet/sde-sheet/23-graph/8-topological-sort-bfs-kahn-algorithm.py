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
Time complexity: O(V + E)
Space Complexity: O(E)
"""

from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        in_degree = [0] * V
        dq = deque()
        result = []
        
        for i in range(len(adj)):
            for item in adj[i]:
                in_degree[item] += 1
        
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                dq.append(i)
        
        while dq:
            node = dq.popleft()
            for adj_node in adj[node]:
                in_degree[adj_node] -= 1
                if in_degree[adj_node] == 0:
                    dq.append(adj_node)
                        
            result.append(node)
        
        return result  
                
                
                