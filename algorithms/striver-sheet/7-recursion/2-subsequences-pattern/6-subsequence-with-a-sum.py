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
