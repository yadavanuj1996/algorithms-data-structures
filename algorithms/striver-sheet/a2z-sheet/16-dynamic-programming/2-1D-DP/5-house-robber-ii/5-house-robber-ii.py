
"""
 House Robber II

Statement
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000

Test Case:

Input: nums = [1,2,3,1]
Output: 4

Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

"""



"""
Time Complexity: O(N),  Because we’ll be traversing the entire array twice.
Space Complexity: O(N ),  Because we’ll be creating an auxiliary array to store the maximum amount robbed for every house.

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if len(nums) == 1:
            return nums[0]
        
        def robMax(n, min_index, memo):
            if n < min_index:
                return 0
            
            if not memo[n] == -1:
                return memo[n]
            
            pick = nums[n] + robMax(n-2, min_index, memo)
            not_picked = 0 + robMax(n-1, min_index, memo)

            memo[n] = max(pick, not_picked)

            return memo[n]
            
        return max(
            robMax(n-1, 1, [-1] * (n)),
            robMax(n-2, 0, [-1] * (n))
        )
            