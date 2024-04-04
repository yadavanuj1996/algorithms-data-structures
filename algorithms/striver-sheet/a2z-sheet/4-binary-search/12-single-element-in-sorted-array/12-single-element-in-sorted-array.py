"""
Single Element in a Sorted Array

Problem Link:
https://leetcode.com/problems/single-element-in-a-sorted-array/

Statement
You are given a sorted array consisting of only integers where every element appears exactly twice, except 
for one element which appears exactly once. Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.


Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5

Test Case:

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

"""

"""
Time complexity: O(log n)
Space complexity: O(1)
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1 or not nums[0] == nums[1]:
            return nums[0]
        
        if not nums[n-1] == nums[n-2]:
            return nums[n-1]

        low = 1
        high = n-2

        while low <= high:
            mid = (low + high) // 2

            if not nums[mid] == nums[mid-1] and not nums[mid] == nums[mid+1]:
                return nums[mid]

            if mid%2 == 0 and nums[mid] == nums[mid+1]:
                low = mid+1
            elif mid%2 == 1 and nums[mid] == nums[mid-1]:
                low = mid+1
            else:
                high = mid-1
