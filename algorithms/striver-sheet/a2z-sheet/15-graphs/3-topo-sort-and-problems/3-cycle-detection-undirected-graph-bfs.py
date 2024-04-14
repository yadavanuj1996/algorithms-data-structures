"""
Detect Cycle in an Undirected Graph

Problem Link:
https://www.codingninjas.com/studio/problems/detect-cycle-in-an-undirected-graph-_758967?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

Statement
Given an undirected graph of 'V' vertices and 'E' edges. Return true if the graph contains a cycle or not, else return false.

Note: There are no self-loops(an edge connecting the vertex to itself) in the given graph.


Constraints:
- 1 <= V <= 10^5
- 0 <= E <= 2 * 10^5
- 0 <= u,v < V


Test Case:

Input: (String) (Read from terminal)
4 4
0 1
1 2
2 3
3 0

Output:  (In form of list)
True

"""

"""
Time complexity: O(N + 2E) + O(N) , roughly equal to O(N+E)
Space Complexity: O(N) , n is no of nodes
"""

from os import *
from sys import *
from collections import *
from math import *

'''

	1. Consider taking input using "stdin" object from the "sys" module for fast I/O
	2. Include the essential imports only 

'''


'''    Do consider the following comments:

	   		1. You have to take the input by yourself as mentioned in the input format.
			2. You have to print the output by yourself as per the output format mentioned.
			3. You may start writing your code below this multi-line comments section.

'''

V, E = input().split()
V, E = int(V), int(E)

node_graph = [[] for i in range(V)]

for i in range(E):
	a, b = input().split()
	a, b = int(a), int(b)
	node_graph[a].append(b)
	node_graph[b].append(a)
	
visited_nodes = [0] * V

dq = deque()

def bfs(node: int, parent_node: int) -> bool:
	dq.append((node, parent_node))

	while dq:
		cur_node = dq[0][0]
		parent_node = dq[0][1]

		if not visited_nodes[cur_node]:
			visited_nodes[cur_node] = 1
			dq.popleft()

			for adj_node in node_graph[cur_node]:
				if not adj_node == parent_node and not adj_node == cur_node:
					dq.append((adj_node, cur_node))
		else:
			return True
		
	return False


result = False
for item in range(V):
	if not visited_nodes[item]:
		if bfs(item, item):
			result = True
			break


print(result)
