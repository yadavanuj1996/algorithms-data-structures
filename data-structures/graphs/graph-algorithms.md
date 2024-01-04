# Graph Algorithms

- DFS
- BFS
- Topological Sort

## DFS
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

![Screenshot 2024-01-04 at 9 01 37 AM](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/f3ea899d-ade9-430a-9ee3-c277ec052413)


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
**Explanation**: The first vertex in topological sorting is always a vertex with an in-degree of 0 (a vertex with no incoming edges).  A topological sorting of the following graph is “5 4 2 3 1 0”. There can be more than one topological sorting for a graph. Another topological sorting of the following graph is “4 5 2 3 1 0”.
