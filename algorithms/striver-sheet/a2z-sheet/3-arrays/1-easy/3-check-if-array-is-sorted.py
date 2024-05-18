""" 
Check if Array Is Sorted and Rotated

Problem Link:
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

Statement
Given an array nums, return true if the array was originally sorted in non-decreasing order, 
then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that 
A[i] == B[(i+x) % A.length], where % is the modulo operation.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100


Test Case:
Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.

"""

"""
Time Complexity: O(N) 
Space Complexity: O(1)
"""
class Solution:
    def check(self, nums: List[int]) -> bool:
        no_of_drops = 0

        if nums[-1] > nums[0]:
            no_of_drops += 1

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                no_of_drops += 1

                if no_of_drops > 1:
                    return False
        
        return True

            
        

        