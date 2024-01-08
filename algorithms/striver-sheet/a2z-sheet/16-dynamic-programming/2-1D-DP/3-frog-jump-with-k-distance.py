
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
# Approach 2: Tabulation

from os import *
from sys import *
from collections import *
from math import *

from typing import *


def frogJump(n: int, heights: List[int]) -> int:
    if n == 1:
        return 0

    memo = [-1]*n

    memo[0] = 0
    memo[1] = abs(heights[1] - heights[0])
    for i in range(2, n):
        memo[i] = min(
            abs(heights[i] - heights[i-1]) + memo[i-1], 
            abs(heights[i] - heights[i-2]) + memo[i-2]
            )

    return memo[n-1]



# Approach 1, memoization
"""
from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    memo = [-1]*n

    def min_energy_req(n):
        if n == 0:
            return 0
        
        if n == 1:
            memo[1] = abs(heights[1] - heights[0])
            return memo[1]
        
        if not memo[n] == -1:
            return memo[n]
        
        memo[n] = min(
                    abs(heights[n]-heights[n-1]) + min_energy_req(n-1),
                    abs(heights[n]-heights[n-2]) + min_energy_req(n-2)
            )
        return memo[n]
    
    return min_energy_req(n-1)


"""
