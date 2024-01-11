"""
0 1 Knapsack

Problem Link:
https://www.codingninjas.com/studio/problems/0-1-knapsack_920542

Statement
A thief is robbing a store and can carry a maximal weight of W into his knapsack. There are N items and the
ith item weighs wi and is of value vi. Considering the constraints of the maximum weight that a knapsack can
carry, you have to find and return the maximum value that a thief can generate by stealing items.

Constraints:
- 1 <= T <= 10
- 1 <= N <= 10^2
- 1<= wi <= 50
- 1 <= vi <= 10^2
- 1 <= W <= 10^3

Test Case:

Sample Input:
1 
4
1 2 4 5
5 4 8 6
5

Sample Output:
13
"""


"""
Solution 1: Memorization Solution

Time Complexity: O(N*W), Reason: There are N*W states therefore at max ‘N*W’ new problems will be solved.
Note: The two for loops that fill dp value to -1, run the code n*w times, also the func get_max_knapsack_val
has two params index and w, so the function can be called with any combination
of index (0 to n) and w (0 to max_weight), thus the time complexity is O(N*W)

Space Complexity: O(N*W) + O(W), We are using a recursion stack space(O(N)) and a 2D array ( O(N*W)).
Dp array has size N*W and recursion stack space is O(W) because we are reducing the val of w
and calling the function again and again.
"""

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
test_cases = int(input())


for _ in range(test_cases):
    n = int(input())
    weights = input().strip().split(" ")
    values = input().strip().split(" ")
    max_weight = int(input())
    for i in range(len(weights)):
        if weights[i]:
            weights[i] = int(weights[i])
        if values[i]:
            values[i] = int(values[i])


    dp = [[-1 for _ in range(max_weight+1)] for _ in range(len(weights))]

    def get_max_knapsack_val(index, w):
        if index == 0:
            if weights[index] <= w:
                return values[index]
            else:
                return 0
        
        
        if not dp[index][w] == -1:
            return dp[index][w]
        
        # pick
        pick = 0
        if w-weights[index] >= 0:
            pick = values[index] + get_max_knapsack_val(index-1, w-weights[index])
        #unpick
        unpick = 0 + get_max_knapsack_val(index-1, w)

        dp[index][w] = max(pick, unpick)
        return dp[index][w]
    
    print(get_max_knapsack_val(n-1, max_weight))
        
    



















"""
