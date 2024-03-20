"""
Subsets II

Problem Link:
https://leetcode.com/problems/subsets-ii

Statement
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

Test Case:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

"""

"""
Approach 1
Time Complexity:
Space Complexity:

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
"""


"""
Approach 2: pick/ unpick and skipping duplicate element using while loop
Time Complexity: O(2^n) ,      for generating every subset and O(k)  to insert every subset in another data structure if the average length of every subset is k. Overall O(k * 2^n).
Space Complexity: O(2^n * k)  ,to store every subset of average length k. Auxiliary space is O(n)  if n is the depth of the recursion tree.
"""
from copy import deepcopy

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        def get_subset_with_dup(index, arr):
            if index == n:
                # Note: We are not searching in result as we are not calling unpick for duplicate 
                # element
                result.append(deepcopy(arr))
                return 
            #pick 
            get_subset_with_dup(index+1, arr+[nums[index]])
            #unpick
            while index+1 < n and nums[index+1] == nums[index]:
                index += 1

            get_subset_with_dup(index+1, arr)
    
        get_subset_with_dup(0, [])
        
        return result
