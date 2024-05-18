""" 
Rotate Array

Problem Link:
https://leetcode.com/problems/rotate-array/

Statement
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- 0 <= k <= 10^5


Test Case:

Input: nums = [1,2,3,4,5,6,7], k = 3

Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

"""

"""
Time Complexity: 
Space Complexity: 
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        while k > n:
            k = k - n
        
        nums[:] = nums[-k:n] + nums[0:-k]