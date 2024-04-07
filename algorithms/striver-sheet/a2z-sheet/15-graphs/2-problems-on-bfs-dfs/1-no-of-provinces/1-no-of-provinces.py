"""
Number of Provinces

Problem Link:
https://leetcode.com/problems/number-of-provinces/

Statement
There are n cities. Some of them are connected, while some are not. If city a is connected directly 
with city b, and city b is connected directly with city c, then city a is connected indirectly with 
city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the 
group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city
are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Constraints:
- 1 <= n <= 200
- n == isConnected.length
- n == isConnected[i].length
- isConnected[i][j] is 1 or 0.
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]


Test Case:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""
"""
Time Complexity: O(N) + O (V+2E) ,O(N) for looping over the no of cites, now for each node
dfs will not run for all the nodes it will run for few nodes and for next node few other dfs call will 
be made in the end it will be summed up to 1 complete dfs(sum of partial dfs calls) and we know
the TC of dfs if O(V+2E)
Space Complexity: O(2N), O(N) for visited array and O(N) for recursion stack
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        no_of_nodes = len(isConnected)
        is_visited = [False] * no_of_nodes
        
        def dfs(cur_node):
            if is_visited[cur_node]:
                return
            # Mark visited
            is_visited[cur_node] = True

            for adj_node in range(no_of_nodes):
                if isConnected[cur_node][adj_node] == 1:
                    dfs(adj_node)
        
        no_of_provinces = 0
        for cur_city_node in range(no_of_nodes):
            if not is_visited[cur_city_node]:
                no_of_provinces += 1
                dfs(cur_city_node)

        return no_of_provinces



