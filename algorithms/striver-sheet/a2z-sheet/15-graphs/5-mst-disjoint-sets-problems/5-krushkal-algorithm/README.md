![IMG_8585](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/2399620e-a3e1-4628-8a20-0fb6769ab58e)

## Algorithm: Kruskal's Minimum Spanning Tree (MST) Algorithm

Input:
- n: Number of nodes in the graph
- edges: List of edges in the graph, each represented as a tuple (u, v, weight),
         where u and v are nodes, and weight is the weight of the edge between them

Output:
- mst_weight: Total weight of the Minimum Spanning Tree (MST) of the graph

Variables:
- rank: An array of size (n+1) to store the rank of each node
- parent: An array of size (n+1) to store the parent of each node
- mst_weight: Total weight of the MST
- edge: Represents an edge in the graph, consists of nodes u and v, and weight

Algorithm Steps:
1. Initialize Disjoint Sets:
   - Initialize rank[i] = 0 for all i in range(1, n+1)
   - Initialize parent[i] = i for all i in range(1, n+1)

2. Define get_ulti_par(node) Function:
   - Purpose: Find the ultimate parent of a node using path compression
   - Implementation: 
     - Recursively traverses the parent pointers of the input node until the ultimate parent is found
     - Updates the parent of intermediate nodes during traversal to optimize future lookups

3. Define union_by_rank(u, v) Function:
   - Purpose: Merge two disjoint sets represented by nodes u and v using union by rank heuristic
   - Implementation:
     - Finds the ultimate parents of nodes u and v
     - Merges the sets by attaching the set with lower rank to the one with higher rank
     - Updates rank and parent arrays accordingly to maintain the rank and parent information of the sets

4. Kruskal's MST Algorithm:
   - Sort all edges of the graph in non-decreasing order of weights
   - Iterate over each edge in the sorted list of edges:
     - For each edge (u, v, weight):
       - If get_ulti_par(u) is not equal to get_ulti_par(v):
         - Add weight to mst_weight
         - Merge the sets containing nodes u and v using union_by_rank(u, v)

5. Return mst_weight as the total weight of the MST

