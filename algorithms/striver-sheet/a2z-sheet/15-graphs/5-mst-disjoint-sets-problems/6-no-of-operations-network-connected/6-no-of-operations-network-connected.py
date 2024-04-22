""" 
Number of Operations to Make Network Connected

Problem Link:
https://leetcode.com/problems/number-of-operations-to-make-network-connected

Statement
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where 
connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other 
computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly
 connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not 
possible, return -1.

Constraints:
- 1 <= n <= 10^5
- 1 <= connections.length <= min(n * (n - 1) / 2, 10^5)
- connections[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no repeated connections.
- No two computers are connected by more than one cable.

The graph is connected.

Test Case:

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

"""

"""
Approach 1: Simple BFS and count required and extra edges

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        visited = [False] * n
        res = []

        # adj list
        adj_list = [[] for _ in range(n)] 
        for connection in connections:
            src_node, dest_node = connection
            adj_list[src_node].append(dest_node)
            adj_list[dest_node].append(src_node)

        def bfs(start_node):
            queue = [start_node]
            comp_nodes = []

            while queue:
                cur_node = queue.pop(0)    
                if visited[cur_node]:
                    continue
                
                comp_nodes.append(cur_node)
                visited[cur_node] = True

                for adj_node in adj_list[cur_node]:
                    queue.append(adj_node)
                        
            
            return comp_nodes
            
            
        total_components = 0
        extra_edges = 0

        for node in range(n):
            nodes_in_comp = []
            if not visited[node]:
                total_components += 1
                nodes_in_comp = bfs(node)

            edges_in_comp = 0
            
            for temp_node in nodes_in_comp:
                edges_in_comp += len(adj_list[temp_node])
            
            edges_in_comp = edges_in_comp // 2
                
            if len(nodes_in_comp) > 0:
                edges_in_comp = edges_in_comp  # as it is bi directional graph so no of edges will be half
                required_edges = len(nodes_in_comp) - 1
                extra_edges += edges_in_comp - required_edges if edges_in_comp - required_edges > 0 else 0
            
        return total_components - 1 if extra_edges >= (total_components-1) else -1

"""

"""
Approach 2: Disjoint Sets

Time Complexity: O(N) + O(E), in detailO(N) + O(N) + O(E* 4 * alpha) + O(N) , N is no of nodes and E is len of connections
4 * alpha is close to 1 so it will treated as constant time
O(n) parent array for loop, O(n) for rank array loop, O(E) for looping over edges and calling union by rank
and get ultimate parents fn call, O(n) for counting no of components for loop

Space Complexity: O(2N), for rank and parent array
"""
class Solution: 
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n

        def get_ultimate_parent(node):
            # base case
            if parent[node] == node:
                return node
            
            ultimate_par = get_ultimate_parent(parent[node])
            parent[node] = ultimate_par
            return parent[node]
        
        def union_by_rank(u, v):
            # Step 1: find ultimate parent of u and v
            ulp_u = get_ultimate_parent(u)
            ulp_v = get_ultimate_parent(v)
            # if two nodes u and v are connected then ultimate parent will be same
            if ulp_u == ulp_v: 
                return
            
            if rank[ulp_u] > rank[ulp_v]:
                parent[ulp_v] = ulp_u
            elif rank[ulp_u] < rank[ulp_v]:
                parent[ulp_u] = ulp_v
            # rank are same
            else:
                parent[ulp_v] = ulp_u
                rank[ulp_u] += 1
        
        no_of_extra_edges = 0

        for edge in connections:
            u, v = edge
            # nodes are already connected and this is not required
            if get_ultimate_parent(u) == get_ultimate_parent(v):
                no_of_extra_edges += 1
            else:
                union_by_rank(u, v)
            
        no_of_components = 0

        for node in range(n):
            # if in parents node all the nodes whose ultimate parents are themselves that means they 
            # are the top element of component , thus total no of components = total no of ultimate parents
            if node == parent[node]:
                no_of_components += 1

        require_edges = no_of_components - 1

        return require_edges if no_of_extra_edges >= require_edges else -1




        

                 
            
            


