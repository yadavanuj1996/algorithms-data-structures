"""
Binary Search

Problem Link:
https://leetcode.com/problems/binary-search/

Statement
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function
to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.

Test Case:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

"""

"""
Time complexity: O(log n)
Space complexity: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.get_element_using_binary_serach(nums, target, 0, len(nums)-1)
    
    def get_element_using_binary_serach(self, nums: list[int], target: int, low: int, high: int) -> int:
        if not low <= high: 
            return -1

        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.get_element_using_binary_serach(nums, target, mid+1, high)
        elif nums[mid] > target:
            return self.get_element_using_binary_serach(nums, target, low, mid-1)
            
        
            

