
"""
House Robber

Statement
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400


Test Case:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

"""



"""
Time Complexity: O(n), 
Space Complexity: O(n), 

"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        memo = [-1] * (n)
    
        def robMax(n):
            if n == 0:
                return nums[n]

            if n < 0:
                return 0
            
            if not memo[n] == -1:
                return memo[n]
            
            pick = nums[n] + robMax(n-2)
            not_picked = 0 + robMax(n-1)
            memo[n] = max(pick, not_picked)

            return memo[n]
        return robMax(n-1)
            