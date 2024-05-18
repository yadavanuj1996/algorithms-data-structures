""" 
Move Zeroes

Problem Link:
https://leetcode.com/problems/move-zeroes/

Statement
Given an integer array nums, move all 0's to the end of it while maintaining the relative 
order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1


Test Case:

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""

"""
Time Complexity: 
Space Complexity: 
"""
"""
Time Complexity: O(N), note we are using two loops but iterating over array only once
Space Complexity: O(1), solved using two pointer approach in constant space
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = None, None

        for ind in range(n):
            # on the first occurence of finding 0 we will set j to index and i to index + 1 and 
            # break the loop
            if nums[ind] == 0:
                j = ind
                i = j+1
                break

        if i is None:
            return nums
        
        # we will run the two pointer approach on the array and the j pointer will always be on the
        # first 0 encountered from left side and when i will reach to a non 0 element we will swap it
        while i < n:
            if not nums[i] == 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

            i += 1
            