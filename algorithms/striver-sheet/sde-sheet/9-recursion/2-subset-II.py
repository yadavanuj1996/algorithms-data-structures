"""
Subsets II

Problem Link:
https://leetcode.com/problems/subsets-ii/description/

Statement
Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10


Test Case:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Input: nums = [0]
Output: [[],[0]]

"""

"""
Time complexity: 
Space Complexity: 
"""

from copy import deepcopy

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        def get_subset_with_dup(index, num, arr):
            if index == n:
                if arr not in result:
                    result.append(deepcopy(arr))
                return 
            #pick 
            arr.append(num[index])
            get_subset_with_dup(index+1, num, arr)
            #unpick
            arr.remove(num[index])
            get_subset_with_dup(index+1,num, arr)
    
        get_subset_with_dup(0, nums, [])
        
        return result
