
"""
Frog Jump

Problem Link:
https://www.codingninjas.com/studio/problems/frog-jump_3621012

Statement
There is a frog on the '1st' step of an 'N' stairs long staircase. The frog wants to reach the 'Nth' stair. 
'HEIGHT[i]' is the height of the '(i+1)th' stair.If Frog jumps from 'ith' to 'jth' stair, the energy lost in 
the jump is given by absolute value of ( HEIGHT[i-1] - HEIGHT[j-1] ). If the Frog is on 'ith' staircase, he
can jump either to '(i+1)th' stair or to '(i+2)th' stair. Your task is to find the minimum total energy used
by the frog to reach from '1st' stair to 'Nth' stair.

For Example
If the given ‘HEIGHT’ array is [10,20,30,10], the answer 20 as the frog can jump from 1st stair to 
2nd stair (|20-10| = 10 energy lost) and then a jump from 2nd stair to last stair (|10-20| = 10 energy lost).
So, the total energy lost is 20.

Constraints:
- 1 <= T <= 10
- 1 <= N <= 100000
- 1 <= HEIGHTS[i] <= 1000 


Test Case:

Input:
2
4
10 20 30 10
3
10 50 10

Output:
20
0

"""



"""
Time Complexity: O(N), 
Space Complexity: O(N), 

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
