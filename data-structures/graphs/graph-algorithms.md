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
**Explanation**: The first vertex in topological sorting is always a vertex with an in-degree of 0 (a vertex with no incoming edges).  A topological sorting of the following graph is “5 4 2 3 1 0”. There can be more than one topological sorting for a 
graph. Another topological sorting of the following graph is “4 5 2 3 1 0”.

![Screenshot 2024-01-04 at 9 19 38 AM](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/085b9bc0-bde6-436e-9b86-3f4d5ed8bc32)



![Screenshot 2024-01-04 at 10 03 58 AM](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/2127ca99-0ec6-43c8-90a8-2764241bb5d6)

