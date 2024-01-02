# Graphs

## Introduction
- A graph is a non-linear data structure consisting of nodes that have data and are connected to other nodes through edges.
- In fact, a tree is a special type of graph with some restriction
- Nodes are circles represented by numbers. Nodes are also referred to as vertices. They store the data. The numbering of the nodes can be done in any order.
- Two nodes are connected by a horizontal line called Edge. Edge can be directed or undirected. Basically, pairs of vertices are called edges.

The graph data structure plays a fundamental role in several applications such as GPS, neural networks, peer-to-peer networks, search engine crawlers, garbage collection (Python), and even social networking websites.

![Screenshot 2022-11-16 at 7 32 32 PM](https://user-images.githubusercontent.com/22169012/202200917-11cbf05e-d4ba-49b7-b249-5065e1ffbc7f.png)

### Graph Structure
A graph is a set of nodes that are connected to each other in the form of a network. First of all, we’ll define the two basic components of a graph.

### Vertex
A vertex is the most essential part of a graph. A collection of vertices forms a graph. In that sense, vertices are similar to linked list nodes.

### Edge
An edge is the link between two vertices. It can be uni-directional or bi-directional depending on your graph. An edge can also have a cost associated with it (will be discussed in detail later).

## Graph Terminologies
- Degree of a Vertex: The total number of edges incident on a vertex. There are two types of degrees:
  - In-Degree: The total number of incoming edges of a vertex.
  - Out-Degree: The total number of outgoing edges of a vertex.
- Parallel Edges: Two undirected edges are parallel if they have the same end vertices. Two directed edges are parallel if they have the same starting and ending vertices.
- Self Loop: This occurs when an edge starts and ends on the same vertex.
- Adjacency: Two vertices are said to be adjacent if there is an edge connecting them directly.


## Representation of Graphs

### Adjacency Matrix
The adjacency matrix is a two-dimensional matrix where each cell can contain a 0 or 1. If a cell contains 1, there exists an edge between the corresponding vertices e.g., Matrix[0][1]=1

Matrix[0][1]=1 shows that an edge exists between vertex 0 and 1. The row and column headings represent the vertices.
 
![Screenshot 2022-11-16 at 7 37 06 PM](https://user-images.githubusercontent.com/22169012/202201938-b3160c4a-52ef-4fcd-8c60-76a2d6f6c5b6.png)


### Adjacency List
An array of linked lists is used to store all the edges in the graph. The size of the array is equal to the number of vertices in the graph. Each index of the array contains a vertex. This vertex points to a linked list that contains all the vertices connected to this one.

- Adjacency List representation is one we will prefer as it saves more space as compare to matrix representation
  
![Screenshot 2022-11-16 at 7 38 28 PM](https://user-images.githubusercontent.com/22169012/202202251-6556a15a-6bfb-487e-85bb-5d8076b9933f.png)


#### Undirected Graph
- If a graph has n vertices then max possible edges are (n*(n-1))/2 (using formula nC2)

#### Directed Graph
- If you have n vertices, then all the possible edges become n*(n-1).


### Types of graph traversals

#### Breadth First Search (BFS)
The BFS algorithm earns its name because it grows breadth-wise. All the nodes at a certain level are traversed before moving on to the next level.
The level-wise expansion ensures that for any starting vertex, you can reach all others, one level at a time.

![Screenshot 2022-11-16 at 7 47 16 PM](https://user-images.githubusercontent.com/22169012/202204319-55a9ba22-8096-490d-8f51-be4d260eb76a.png)

#### Depth First Search (DFS)
The DFS algorithm is the opposite of BFS in the sense that it grows depth-wise.

Starting from any node, we keep moving to an adjacent node until we reach the farthest level. Then we move back to the starting point and pick another adjacent node. Once again, we probe to the farthest level and move back. This process continues until all nodes are visited.

![Screenshot 2022-11-16 at 7 47 54 PM](https://user-images.githubusercontent.com/22169012/202204441-158c1616-fd57-4d4e-92a9-615d742582ed.png)


**Note: Please note the breadth is measured by how far it is from the selected node. The level is measured not by whether it is down or above in graph it is judged by how far it is from the node we are selectin in Graph. Similar concept applies in DFS as well.**

## Connected Components

![Screenshot 2024-01-02 at 12 33 20 PM](https://github.com/yadavanuj1996/algorithms-data-structures/assets/22169012/f5f8c6de-e56f-43bc-acde-98efb3f51426)

The above is one graph with 4 components.
Note: The graph might have nodes that are not connected to any other node of graph.

The graph can be represented using
```
N = 10 (total nodes)
E = 8 (Total edges)

Adjacency List of above graph
1 2
1 3
2 4 
3 4
5 6
5 7
6 7 
8 9
```

### References & Links:
- https://www.youtube.com/watch?v=M3_pLsDdeuU&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=1 (striver)
