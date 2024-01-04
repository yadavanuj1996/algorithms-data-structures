
"""
Jump Game

Statement
You are given an integer array nums. You are initially positioned at the array's first index, and each element
in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^5


Test Case:

Input: nums = [2,3,1,1,4]
Output: true

Input: nums = [3,2,1,0,4]
Output: false

"""



"""
Time Complexity: O(n), 
Space Complexity: O(1), 

"""

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
               return False
            
            reachable = max(reachable, nums[i] + i)
        
        return True