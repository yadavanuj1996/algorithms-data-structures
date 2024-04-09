"""
Is Graph Bipartite?

Problem Link:
https://leetcode.com/problems/is-graph-bipartite/

Statement
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 
2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in 
graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

- There are no self-edges (graph[u] does not contain u).
- There are no parallel edges (graph[u] does not contain duplicate values).
- If v is in graph[u], then u is in graph[v] (the graph is undirected).
- The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.

A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in 
the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.



Constraints:
- graph.length == n
- 1 <= n <= 100
- 0 <= graph[u].length < n
- 0 <= graph[u][i] <= n - 1
- graph[u] does not contain u.
- All the values of graph[u] are unique.
- If graph[u] contains v, then graph[v] contains u.


Test Case:

Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a
node in one and a node in the other.
"""

"""
Time Complexity: O(V)
Space complexity: O(V), actually O(3V) visited and is_colored and recursion stack each has O(V) or O(N) space comp.
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph) 
        visited = [False] * n
        is_colored = [None] * n

        def color_node(cur_node, color=True):
            if visited[cur_node]:
                return False if not is_colored[cur_node] == color else True
            
            visited[cur_node] = True
            is_colored[cur_node] = color

            is_bipartite = True
            for adj_node in graph[cur_node]:
                is_bipartite = is_bipartite and color_node(adj_node, not color)
            
            return is_bipartite
            
            
        for node in range(n):
            # This check is critical
            if visited[node]:
                continue

            if not color_node(node):
                return False
        
        return True
        
        
            
            
            

