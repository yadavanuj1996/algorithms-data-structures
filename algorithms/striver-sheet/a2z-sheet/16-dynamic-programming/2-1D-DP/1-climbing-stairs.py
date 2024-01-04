"""
Problem Link: https://leetcode.com/problems/climbing-stairs/description/

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)
        memo[0]= memo[1] = 1

        for i in range(2, n+1):
            memo[i] = memo[i-1] + memo[i-2]
        
        return memo[n]

"""

Time Complexity: O(n)
Space Complexity: O(n)
"""
     
"""
Alternate Approach

class Solution:
    
    def climbStairs(self, n: int) -> int:
        return self.climbStairRecursion(n, {})

    def climbStairRecursion(self, n:int, memo: dict) -> int:
        if memo.get(n):
            return memo[n]
        
        if n == 0:
            return  1
        
        if n < 0:
            return 0
        
        memo[n] = self.climbStairRecursion(n-1, memo) + self.climbStairRecursion(n-2, memo) 
        return memo[n]
        
        
"""