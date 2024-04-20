# Graph Algorithms

- DFS
- BFS
- Topological Sort

## DFS
DFS is a traversal technique which involves the idea of recursion and backtracking. DFS goes in-depth, i.e., traverses all nodes by going ahead, and when there are no further nodes to traverse in the current path, then it backtracks on the same path and traverses other unvisited nodes. 

- In DFS, we start with a node ‘v’, mark it as visited and store it in the solution vector. It is unexplored as its adjacent nodes are not visited.
- We run through all the adjacent nodes, and call the recursive dfs function to explore the node ‘v’ which has not been visited previously. This leads to the exploration of another node ‘u’ which is its adjacent node and is not visited. 
- The adjacency list stores the list of neighbours for any node. Pick the neighbour list of node ‘v’ and run a for loop on the list of neighbours (say nodes ‘u’ and ‘w’ are in the list). We go in-depth with each node. When node ‘u’ is explored completely then it backtracks and explores node ‘w’.
- This traversal terminates when all the nodes are completely explored. 

![Screenshot 2024-01-04 at 9 02 33 AM](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/8dc9a3e4-e814-4fbb-a86b-c84d8b106181)

```
def dfs(cur_node):
    if not visited_nodes[cur_node]:
        visited_nodes[cur_node] = 1
        result.append(cur_node)
        
        for adj_node in adj[cur_node]:
            dfs(adj_node)
    
```

## BFS
Initial Configuration:
- Queue data structure: follows FIFO, and will always contain the starting.
- Visited array: an array initialized to 0

- In BFS, we start with a “starting” node, mark it as visited, and push it into the queue data structure.
- In every iteration, we pop out the node ‘v’ and put it in the solution vector, as we are traversing this node.
- All the unvisited adjacent nodes from ‘v’ are visited next and are pushed into the queue. The list of adjacent neighbors of the node can be accessed from the adjacency list.
- Repeat steps 2 and 3 until the queue becomes empty, and this way you can easily traverse all the nodes in the graph.

```
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

    
```

## Topological Sort
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u-v, 
vertex u comes before v in the ordering.

Note: Topological Sorting for a graph is not possible if the graph is not a DAG.\

**Exapmple:**  
Input:   
![topological-example](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/83c459ec-8171-46d7-a7d2-01ecc8a33b86)


**Output**: 5 4 2 3 1 0  
**Explanation**: The first vertex in topological sorting is always a vertex with an in-degree of 0 (a vertex with no incoming edges).  A topological sorting of the following graph is “5 4 2 3 1 0”. There can be more than one topological sorting for a 
graph. Another topological sorting of the following graph is “4 5 2 3 1 0”.


### Topo sort using DFS
Stack based approach 
Here we are exploring all the adjacent nodes before printing/ selecting the node itself( this is different from simple DFS)

```
def topoSort(node):
    if visited[node]:
        return

    visited[node] = True
    for adj_node in graph[node]:
        topoSort(adj_node)

    stack.append(node)
```

![IMG_4852](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/15975f3a-bc0c-454c-abab-9b8b35a976c9)


### Topo sort using BFS (Kahn Algorithm)
Here we are using a Queue and in-degree array to do topo sort

![IMG_4857_2](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/6ca410d5-c357-4f43-b91b-b6da23b3967c)

```
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
    
```

## Dijstras Algorithm
![IMG_8351](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/93cef1a9-eb00-4fd5-ac0e-dffe6e37e5a9)

```
# setting up dist and priority queue
dist = [float("inf")] * vertices
priority_queue = []             # Add (dist, node)

# setting up source node distance and adding it to priority queue
dist[source] = 0
heappush(priority_queue, (dist[source], source))

while priority_queue:
    # this will pop the item that will have min distance
    cur_path_dis, cur_node = heappop(priority_queue)
    
    for adj_node_detail in adj_list[cur_node]:
        adj_node = adj_node_detail[0]
        adj_node_dist = adj_node_detail[1]
        
        if cur_path_dis + adj_node_dist < dist[adj_node]:
            dist[adj_node] = cur_path_dis + adj_node_dist
            
            heappush(priority_queue, (dist[adj_node], adj_node))
            
return dist
```

## Bellman Ford
![IMG_8502](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/e4bfbd2e-463c-42b3-8268-27b506b5307d)
![IMG_8503](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/6a008d33-88e2-42cc-bcdb-137bc50b53a5)
![IMG_8504](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/97e5a3b3-3820-4365-9253-900e42fab51c)

```
def bellmonFord(n, m, src, edges):
    dist = [10**8] * (n+1)
    # for source node dist is 0
    dist[src] = 0
    # for n-1 relaxation 
    for i in range(n-1):
        # sequentially relaxing each edge
        for edge in edges:
            s_node, d_node, weight = edge
            if dist[s_node] + weight < dist[d_node]:
                dist[d_node] = dist[s_node] + weight

    return dist
```

## Floyd Warshal
![IMG_8505](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/12c9a5dd-47be-440c-aa70-f17b69d14cd6)
![IMG_8506](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/8dbdb1fc-158f-4ca3-94ef-54be807d717f)
![IMG_8508](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/23c44172-c476-4557-b414-d0ef1fb0fbd3)

```
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
    
    
```

## Minimum Spanning Tree
- Spanning Tree: A spanning tree is a tree in which we have N nodes(i.e. All the nodes present in the original graph) and N-1 edges and all nodes are reachable from each other.

**Minimum Spanning Tree:**
Among all possible spanning trees of a graph, the minimum spanning tree is the one for which the sum of all the edge weights is the minimum.

Two algorithms are present for finding minimum spanning tree
- Prim's algorithm
- Krushkal's algorithm

Graph:  
![1](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/72b275de-90c9-42e8-bef6-25dc7a4f6400)

Minimum Spanning Tree:  
![2](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/d479685a-776f-477e-b362-40744f7a1616)

### Prim's Algorithm
![IMG_8511](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/71c21459-ad77-492b-a0eb-0f79740be8e2)
![IMG_8512](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/f2255bfe-a30c-43c6-92f7-0d1c2dfc1ac1)

```
def minimumSpanningTree(adj_list, V, E):
    # your code goes here
    visited = [False] * V
    priority_queue = []
    mst_edges = []
    mst_weight = 0


    heappush(priority_queue, (0, 0, -1)) # (dist, cur_node, parent_node)
    
    while priority_queue:
        edge_weight, cur_node, parent_node = heappop(priority_queue)
        if visited[cur_node]:
            continue
        
        visited[cur_node] = True

        if not parent_node == -1:
            mst_edges.append((parent_node, cur_node))
            mst_weight += edge_weight
        
        for adj_node_details in adj_list[cur_node]:
            adj_node, adj_node_weight = adj_node_details
            # we are checking again to not add extra edges in PQ thus improving time complexity
            if not visited[adj_node]:
                heappush(priority_queue, (adj_node_weight, adj_node, cur_node))




    return mst_weight
```

#### Disjoint set (Prerequisite for kruskal's algorithm)

![IMG_8582](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/9b107d28-36eb-4fcd-812c-1f5590c25fe4)
![IMG_8583](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/29647080-33e9-4b97-b615-d5d96990bf99)
![IMG_8584](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/b6b5caa9-1c07-4162-9ed7-e3b6bf5eb992)

