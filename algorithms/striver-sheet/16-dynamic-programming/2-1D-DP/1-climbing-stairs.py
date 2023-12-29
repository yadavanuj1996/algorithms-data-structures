"""
Problem Link: https://leetcode.com/problems/climbing-stairs/description/

Time Complexity: O(n)
Space Complexity: O(n)
"""

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
        
        
        