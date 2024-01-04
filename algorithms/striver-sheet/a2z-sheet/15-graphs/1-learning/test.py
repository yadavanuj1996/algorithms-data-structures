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
print(node_graph)


def bfs(node, parent_node):
	dq = deque([node])
    print(node, parent_node)
	while dq:
		cur_node = dq.popleft()
		if not visited_nodes[cur_node]:
			visited_nodes[cur_node] = 1
			for adj_node in node_graph[cur_node]:
				if not adj_node == parent_node:
				    dq.append(adj_node)		
		else:
			return True

	return False


result = False

for item in range(V):
	if not visited_nodes[item]:
		val = bfs(item, item) 
		print(item, val)
		if val:
			result = True
			break

print(result)





