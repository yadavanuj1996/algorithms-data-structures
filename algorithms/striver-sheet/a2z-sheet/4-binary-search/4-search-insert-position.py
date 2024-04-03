"""
Implement Upper Bound

Problem Link:
https://leetcode.com/problems/search-insert-position/

Statement
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order.
- -10^4 <= target <= 10^4

Test Case:

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

"""

"""
Time complexity: O(log n)
Space complexity: O(1)
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        higher_bound = n
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] < target:
                low = mid + 1
            elif  nums[mid] > target:
                higher_bound = mid
                high = mid - 1
            else:
                return mid

        return higher_bound
        