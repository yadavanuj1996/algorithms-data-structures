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
