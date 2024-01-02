"""
Find the no of provinces

Problem Link:
https://www.codingninjas.com/studio/problems/find-the-number-of-states_1377943?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

Statement
You are given ‘n’ cities, SOME of which are connected by bidirectional roads. 
You are also given an ‘n x n’ matrix i.e. ‘roads’, where if city ‘i’ and ‘j’ are connected by a road then
‘roads[i][j]'= 1, otherwise ‘roads[i][j]' = 0.

A province is a group of cities that are either directly or indirectly connected to each other through roads.

The goal is to count and return the total number of such provinces in the given matrix.

Constraints:
- 1 <= 'n' <= 200
- roads[i][j] is 1 or 0.
- roads[i][j] == roads[j][i]



Test Case:

Input: 
3
1 0 0 
0 1 0 
0 0 1 

Output: 3

Input: 
4
1 1 0 0 
1 1 0 0 
0 0 1 1 
0 0 1 1 

Output: 2

"""

from typing import List

def findNumOfProvinces(roads: List[List[int]], n: int) -> int:
    res = 0
    visited_nodes = [0]*n

    def dfs(node):
        if visited_nodes[node] == 1:
            return
        
        visited_nodes[node] = 1

        for connecting_node in range(len(roads[node])):
            if roads[node][connecting_node] == 1:
                dfs(connecting_node)
        
    for cur_node in range(n):
        if visited_nodes[cur_node] == 0:
            res += 1
            dfs(cur_node)

    return res