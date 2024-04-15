"""
Find Eventual Safe States

Problem Link:
https://leetcode.com/problems/find-eventual-safe-states/

Statement
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented
by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, 
meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible
path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending 
order.

Constraints:
- n == graph.length
- 1 <= n <= 10^4
- 0 <= graph[i].length <= n
- 0 <= graph[i][j] <= n - 1
- graph[i] is sorted in a strictly increasing order.
- The graph may contain self-loops.
- The number of edges in the graph will be in the range [1, 4 * 10^4].



Test Case:

Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]

Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.


"""


"""
Approach 1: Simple recursion using dfs 


Time Complexity: O(V log V) , actually in detail O(V) + O(V) + O(V) + O(V log V)
O(V) for checking len of graph, O(V) for creating visiting arr, O(V) for iterating over node and
calling eventual states fn Note: even the for loop in eventual_nodes is there but overall the fn
will only be called only once for each node, O(V log V) for sorting

Space Complexity: O(V) + O(V)
O(V) for visited array, O(V) for recursion stack in worst case fn will be called for all the nodes

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        visited = [False] * V
        result = []

        def eventual_states(cur_node):
            if visited[cur_node]:
                return True if cur_node in result else False

            visited[cur_node] = True
            # check it it's a terminal node
            if len(graph[cur_node]) == 0:
                result.append(cur_node)
                return True
            
            # iterate over all neighbouring nodes
            res = True
            for adj_node in graph[cur_node]:
                res = res and eventual_states(adj_node)
                if not res:
                    return False
            
            result.append(cur_node)
            return True
            

        for node in range(V):
            if not visited[node]:
                eventual_states(node)
        
        result.sort()
        return result

"""

"""
Topo sort solution approach
Time Complexity: O(V) + O(V) + O(V+E) + O(V+E) + O(V) + O(V log V)
O(V) for setting up reverse graph, O(V) for in degree, O(V*E) for nested loops of reverse edges, 
O(V*E) for in degree, O(V) for looping over the queue for topo sort nested loops, O(V log V) for
sorting the result arr

Space Complexity: O(V+E), in detail it was O(V+E) + O(V) + O(V) + O(V)
O(V*E) for creating reverse graph, O(V) for in degree, O(V) for adding nodes Queue (worst case all
nodes will be added), O(V) for result array
"""
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        result = []
        reverse_graph = [[] for _ in range(V)]
        in_degree = [0] * V
        queue = []
        # reverse edges of the graph
        for cur_node in range(V):
            # Note: in degree is for reverse graph , so for original graph i am calculating out degree
            # that will be equal to in degree of reverse graph
            in_degree[cur_node] = len(graph[cur_node])
            for adj_node in graph[cur_node]:
                reverse_graph[adj_node].append(cur_node)
        
        # add 0 in-degree nodes to queue
        for cur_node in range(V):
            if in_degree[cur_node] == 0:
                queue.append(cur_node)

        # Topo sort using queue, BFS
        while queue:
            cur_node = queue.pop(0)
            result.append(cur_node)

            for adj_node in reverse_graph[cur_node]:
                in_degree[adj_node] -= 1

                if in_degree[adj_node] == 0:
                    queue.append(adj_node)
        
        result.sort()
        return result



                
         
        
        

        