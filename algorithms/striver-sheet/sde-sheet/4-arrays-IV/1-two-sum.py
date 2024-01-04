
"""
Two Sums

Link: https://leetcode.com/problems/two-sum/

Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Test Case:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]

Constraints:

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9


Tags: 
two-pointer, sorting
"""

"""
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
import copy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original_input = copy.deepcopy(nums)
        nums.sort()
        i, j = 0, len(nums) - 1
        fir_ind, sec_ind = -1, -1
        while i < j:
            if nums[i] + nums[j] == target:
                break
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1

        for ind in range(len(original_input)):
            if original_input[ind] == nums[i] and fir_ind == -1:
                fir_ind = ind 
            elif original_input[ind] == nums[j]:
                sec_ind = ind

        return [fir_ind, sec_ind]


       