
"""
 Subsets

Statement
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10

Test Case:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]

"""



"""
Time Complexity: O(2^n), 
Space Complexity: O(n), 

"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        result = []
        def generateSubset(index, cur_set, nums):
            if index == len(nums):
                result.append(cur_set.copy())
                return 
                
            # pick 
            cur_set.append(nums[index])
            generateSubset(index+1, cur_set, nums)
            # unpick 
            cur_set.remove(nums[index])
            generateSubset(index+1, cur_set, nums)

            
    
        generateSubset(0, [], nums)
        return result      
    