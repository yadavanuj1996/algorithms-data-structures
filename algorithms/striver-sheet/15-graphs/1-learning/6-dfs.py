"""
DFS of Graph

Problem Link:
https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

Statement
You are given a connected undirected graph. Perform a Depth First Traversal of the graph.
Note: Use the recursive approach to find the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph.

Constraints:
- 1 ≤ V, E ≤ 10^4



Test Case:


Input:
V = 5 , adj = [[2,3,1] , [0], [0,4], [0], [2]]

Output:  (In form of list)
0 2 4 3 1

"""

"""
Time complexity: O(N) + O(E)  (O(N) + O(2E)), n is nodes & e is no of edges 
Space Complexity: O(V)
"""

#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited_nodes = [0] * V
        total_dis_comp = 0
        result = []
    
        def dfs(cur_node):
            if not visited_nodes[cur_node]:
                visited_nodes[cur_node] = 1
                result.append(cur_node)
                
                for adj_node in adj[cur_node]:
                    dfs(adj_node)
    
        for node in range(V):
            if not visited_nodes[node]:
                total_dis_comp += 1
                dfs(node)
                
        return result
    
        


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends