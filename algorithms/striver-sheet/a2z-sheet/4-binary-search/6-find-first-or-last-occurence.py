"""
Find First and Last Position of Element in Sorted Array

Problem Link:
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Statement
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a 
given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums is a non-decreasing array.
- -10^9 <= target <= 10^9

Test Case:

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

"""

"""
Time complexity: O(n), if all the elements in array will be same it will iterate over the whole array
Space complexity: O(1)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        low, high = 0, n-1
        res = [-1, -1]
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                temp_ind = mid
                while temp_ind < n and nums[temp_ind] == target:
                    res[1] = temp_ind
                    temp_ind += 1
                
                temp_ind = mid
                while temp_ind >= 0 and nums[temp_ind] == target:
                    res[0] = temp_ind
                    temp_ind -= 1
                
            
            if nums[mid] < target:
                low = mid + 1
            
            if  nums[mid] >= target:
                high = mid - 1
            
        return res
                            
           
    
                        
           
    
        