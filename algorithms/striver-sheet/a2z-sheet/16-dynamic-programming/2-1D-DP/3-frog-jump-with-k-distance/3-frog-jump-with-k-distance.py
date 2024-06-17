
"""
Minimal Cost

Problem Link:
https://www.codingninjas.com/studio/problems/minimal-cost_8180930

Statement
There is an array of heights corresponding to 'n' stones. You have to reach from stone 1 to stone ‘n’.

From stone 'i', it is possible to reach stones 'i'+1, ‘i’+2… ‘i’+'k' , and the cost incurred will be
| Height[i]-Height[j] |, where 'j' is the landing stone.

Return the minimum possible total cost incurred in reaching the stone ‘n’.

Constraints:
- 1 <= n <= 10^4
- 1 <= k <= 100
- 1 <= height[i] <= 10^4
- Time Limit: 1 sec


Test Case:

Input:
4 2
10 40 30 10

Output:
40

Explanation of sample output 1:
For ‘n’ = 4, 'k' = 2, height = {10, 40, 30, 10}
"""



"""
Time Complexity: O(N*K),  n is total no of steps and k is no of steps allowed 
Space Complexity: O(N)

"""
from typing import *

def minimizeCost(n : int, k : int, heights : List[int]) -> int:
    # Write your code here.
    memo = [-1]*n

    def min_energy_req(n):
        if n == 0:
            return 0
        
        if not memo[n] == -1:
            return memo[n]

        if n == 1:
            memo[1] = abs(heights[1]-heights[0])
            return memo[1]
        
        minimum = float("inf")

        for i in range(1, k+1):
            if n-i >= 0 :
                val = abs(heights[n]-heights[n-i]) + min_energy_req(n-i)
                minimum = min(minimum, val)
        
        memo[n] = minimum
        return memo[n]
    
    return min_energy_req(n-1)

        
        
    
