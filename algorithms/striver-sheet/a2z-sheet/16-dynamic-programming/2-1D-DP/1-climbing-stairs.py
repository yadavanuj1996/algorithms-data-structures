"""
Problem Link: https://leetcode.com/problems/climbing-stairs/description/

Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Constraints:
1 <= n <= 45

Test Cases:
Input: n = 2
Output: 2

Input: n = 3
Output: 3


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
