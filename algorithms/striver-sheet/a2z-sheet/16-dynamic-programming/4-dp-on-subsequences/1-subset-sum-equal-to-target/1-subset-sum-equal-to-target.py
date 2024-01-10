"""
Subset Sum Equal To K

Problem Link:
https://www.codingninjas.com/studio/problems/subset-sum-equal-to-k_1550954

Statement
You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

For Example :
If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.

Constraints:
- 1 <= T <= 5
- 1 <= N <= 10^3
- 0 <= ARR[i] <= 10^9
- 0 <= K <= 10^3
- Time Limit: 1s

Test Case:

Input
2
4 5
4 3 2 1
5 4
2 5 1 6 7

Output :
true
false

"""


"""
Time Complexity: O(N*K) 
Space Complexity: O(N*K)

"""
from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
    memo = [[-1 for j in range(k+1)] for i in range(n)]

    def get_subset_sum_to_k(index, target):
        if target == 0:
            return True
        
        if target < 0:
            return False

        if index == 0:
            return arr[index] == target
        
        if not memo[index][target] == -1:
            return memo[index][target]
        
        # pick 
        pick = get_subset_sum_to_k(index-1, target-arr[index])
        # unpick
        unpick = get_subset_sum_to_k(index-1, target)
    
        memo[index][target] = pick or unpick
        return memo[index][target]

    return get_subset_sum_to_k(n-1, k)








    
    
    

