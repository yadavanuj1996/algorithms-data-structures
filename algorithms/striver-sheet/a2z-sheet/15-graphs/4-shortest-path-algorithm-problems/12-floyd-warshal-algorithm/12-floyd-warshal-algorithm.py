""" 
Floyd Warshall

Problem Link:
https://www.naukri.com/code360/problems/floyd-warshall_2041979

Statement
You have been given a directed weighted graph of ‘N’ vertices labeled from 1 to 'N' and ‘M’ edges. Each edge 
connecting two nodes 'u' and 'v' has a weight 'w' denoting the distance between them.

Your task is to find the length of the shortest path between the ‘src’ and ‘dest’ vertex given to you in the 
graph using Flloyd warshall’s algorithm. The graph may contain negatively weighted edges.

Note :

It's guaranteed that the graph doesn't contain self-loops and multiple edges. Also, the graph does not contain 
negative weight cycles.

Constraints:
- 1 <= T <= 10
- 1 <= N <= 50
- 1 <= M <= 300
- 1 <= src <= N
- 1 <= u,v <= N
- -10^5 <= w <= 10^5
- Time Limit: 1 sec

Test Case:

Sample Input 1 :
1    
4 4 1 4
1 2 4
1 3 3
2 4 7 
3 4 -2

Sample Output 1 :
1
"""

"""
Time Complexity: O(n^3), in detail O(V^2) + O(V^2) + O(E) + O(V^3), n is no of vertices & m is no of edges. 
O(V^3) due to 3 for loops using via and src and dest node iteration

Space Complexity: O(n^2), in details n is no vertices so O(V^2)
"""
def floydWarshall(n, m, src, dest, edges):
    # Write your code here.
    # Note we are using n+1 as the node index start from 1 and not 0
    # Step 1: Create a dist_matrix 2d array with unreachable values infinity
    dist_matrix = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]

    # Step 2: set all nodes that point to themselves as 0, as reaching itself takes 0 
    # distance and no self loop is possible
    for s_node in range(1, n+1):
            for d_node in range(1, n+1):
                if s_node == d_node:
                    dist_matrix[s_node][d_node] = 0
    
    # Step 3: set values if edges directly connect two nodes, setup dist_matrix values 
    # on the basis of edges
    for edge in edges:
        s_node, d_node, weight = edge
        dist_matrix[s_node][d_node] = weight

    # Step 4: travel from each node to all other nodes using a via node logic
    for via_node in range(1, n+1):
        for s_node in range(1, n+1):
            for d_node in range(1, n+1):
                dist_matrix[s_node][d_node] = min(dist_matrix[s_node][d_node], dist_matrix[s_node][via_node] + dist_matrix[via_node][d_node])

    # Note: in the problem if the node cannot be reached we need to return 10^9
    return dist_matrix[src][dest] if not dist_matrix[src][dest] == float("inf") else 10**9
    
    

