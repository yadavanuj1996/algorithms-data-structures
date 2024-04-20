""" 
Kruskal’s Minimum Spanning Tree Algorithm

Problem Link:
https://www.naukri.com/code360/problems/kruskal%E2%80%99s-minimum-spanning-tree-algorithm_1082553

Statement
A minimum spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all 
the vertices without any cycles and with the minimum possible total edge weight.

A spanning tree’s weight is the sum of the weights of each edge in the spanning tree.
You have been given a connected undirected weighted graph having 'n' vertices, from 1 to 'n', and 'm' edges.
You are given an array 'edges' of size 'm', containing the details of the edges of the graph.

Each element of 'edges' contains three integers, the two vertices that are being connected and the weight of the edge.

Find the weight of the minimum spanning tree of the given graph.

Constraints:
- 2 <= 'n' <= 10000
- n-1 <= 'm' <= min(10000, n * (n-1) / 2)
- 1 <= 'w' <= 10000
- 1 <= 'u', 'v' <= n

The graph is connected.

Test Case:

Sample Input 1:
5 6
1 2 6
2 3 5
3 4 4
1 4 1
1 3 2
3 5 3


Sample Output 1:
11
"""

"""
Time Complexity: O(E logE) + O(E*4α*2)   where N = no. of nodes and E = no. of edges. O(E logE) for sorting the array consists of the edge tuples. 
Finally, we are using the disjoint set operations inside a loop. The loop will continue to E times. Inside that 
loop, there are two disjoint set operations like findUPar() and UnionBySize() each taking 4 and so it will result
 in 4*2. That is why the last term O(E*4*2) is added.

Space Complexity: O(N) + O(N) + O(E) where E = no. of edges and N = no. of nodes. O(E) space is taken by the array
that we are using to store the edge information. And in the disjoint set data structure, we are using two N-sized
arrays i.e. a parent and a size array (as we are using unionBySize() function otherwise, a rank array of the same 
size if unionByRank() is used) which result in the first two terms O(N).
"""
from typing import List

def kruskalMST(n: int, edges: List[List[int]]) -> int:
    # Write your code here
    # First we will write algorithm for finding disjoint sets
    # initializng rank and parent for dijoint sets
    rank = [0] * (n+1)
    parent = [i for i in range(n+1)]

    # get ultimate parent fn
    def get_ulti_par(node):
        # base case
        if parent[node] == node:
            return node
        
        ultimate_parent = get_ulti_par(parent[node])
        parent[node] = ultimate_parent
        return parent[node]
    
    # union by rank fn
    def union_by_rank(u, v):
        # step 1 : find ultimate parent of u and v
        u_ult_par = get_ulti_par(u)
        v_ult_par = get_ulti_par(v)

        # check if the ultimate parents are same then do nothing
        # as it means the nodes ultimate parent are already connected
        if u_ult_par == v_ult_par:
            return
        
        if rank[u_ult_par] < rank[v_ult_par] :
            parent[u_ult_par] = v_ult_par
        elif rank[u_ult_par] > rank[v_ult_par] :
            parent[v_ult_par] = u_ult_par
        # if rank are same add any one 
        else:
            parent[v_ult_par] = u_ult_par
            rank[u_ult_par] += 1

    # Krushkal's main MST algo start here
    mst_weight = 0
    # Step 1: sort all edges according to weights
    edges.sort(key=lambda element: element[2])

    # Step 2: iterate over each edge in increasing weight order
    for edge in edges:
        u, v, weight = edge
        # Step 3: condition check if it's not already connected in MST
        # if not then add the edge to mst and weight to mst weight
        # and call union by rank to merge the two node's ultimate 
        # parents with each other
        if not get_ulti_par(u) == get_ulti_par(v):
            mst_weight += weight
            union_by_rank(u, v)
    
    return mst_weight
        