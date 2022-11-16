# Graphs

## Introduction
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

![Screenshot 2022-11-16 at 7 38 28 PM](https://user-images.githubusercontent.com/22169012/202202251-6556a15a-6bfb-487e-85bb-5d8076b9933f.png)

