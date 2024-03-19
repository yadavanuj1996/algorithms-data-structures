"""
Note: This problem was solved using recursion alone in first iteration, but we have imporoved time
complexity by adding Dynamic programming solutin in iteration 2
Problem Link:
https://www.codingninjas.com/studio/problems/subset-sum_630213?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

"""

"""
Iteration 1
Time Complexity: O(2^n) 
Space Complexity: O(n)
"""

"""
from typing import *

def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    # Write your code here.
    return find(0, 0 , a, n, k)

def find(index, sum, nums, n, k):
    if sum > k: 
        return False
        
    if index == n:
        if sum == k:
            return True
        else:
            return False

    # pick 
    if find(index+1, sum+nums[index], nums, n, k):
        return True
    # unpick
    if find(index+1, sum, nums, n, k):
        return True
    
    return False

"""

"""
Iteration 2 (DP Solution)

Time Complexity: O(n * k) 
Space Complexity: O(n * k) 
"""
from typing import *

def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    # Write your code here.
    nums = a
    memo = [[-1]*(k+1)]*(n+1)

    
    def find(index, sum):
        if sum > k: 
            return False
        
        if not memo[index][sum] == -1:
            return memo[index][sum]
            
        if index == n:
            if sum == k:
                #print("inde -> ",index," sum -> ", sum)
                memo[index][sum] = True
                return True
            else:
                memo[index][sum] = False
                return False

        # pick 
        if find(index+1, sum+nums[index]):
            return True
        # unpick
        if find(index+1, sum):
            return True
        
        return False

    return find(0, 0)
