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
        # soldier problem: A A B B C D D
        #                  0 1 2 3 4 5 6
        # If nums[even] == nums[even+1], the pair is intact and the broken
        # soldier (single element) lies to the right; otherwise it's on this
        # soldier or to the left. Loop ends with left == right at the answer.
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2

            if mid % 2 != 0:
                mid = mid - 1

            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]
