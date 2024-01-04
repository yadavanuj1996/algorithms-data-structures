# Graph Algorithms

- DFS
- BFS
- Topological Sort

## Topological Sort
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u-v, 
vertex u comes before v in the ordering.

Note: Topological Sorting for a graph is not possible if the graph is not a DAG.\


**Exapmple:**  
Input:   
![topological-example](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/83c459ec-8171-46d7-a7d2-01ecc8a33b86)


**Output**: 5 4 2 3 1 0  
**Explanation**: The first vertex in topological sorting is always a vertex with an in-degree of 0 (a vertex with no incoming edges).  A topological sorting of the following graph is “5 4 2 3 1 0”. There can be more than one topological sorting for a graph. Another topological sorting of the following graph is “4 5 2 3 1 0”.
