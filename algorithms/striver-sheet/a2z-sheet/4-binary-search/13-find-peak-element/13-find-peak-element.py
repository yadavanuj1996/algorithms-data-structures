"""
Search Insert Position

Problem Link:
https://leetcode.com/problems/find-peak-element/

Statement
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple
peaks, return the index to any of the peaks. 
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly 
greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Constraints:
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i.

Test Case:

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 
where the peak element is 6.

"""

"""
Time complexity: O(log n)
Space complexity: O(1)
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 1, n-2

        if n == 1:
            return 0

        if nums[0] > nums[1]:
            return 0
        
        if nums[n-1] > nums[n-2]:
            return n-1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid

            if nums[mid] > nums[mid+1]:
                high = mid-1
            elif  nums[mid] < nums[mid+1]:
                low = mid + 1
                
           
    
                        
           
    
        