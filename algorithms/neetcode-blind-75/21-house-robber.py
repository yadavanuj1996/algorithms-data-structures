"""
TC: O(n)
SC: O(n) memo + O(n) recursion stack

Check older solution not this one
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * (n)

        def robMax(n, min_index):
            if n < min_index:
                return 0

            if not memo[n] == -1:
                return memo[n]

            pick = nums[n] + robMax(n-2, min_index)
            not_picked = 0 + robMax(n-1, min_index)

            memo[n] = max(pick, not_picked)

            return memo[n]
        return robMax(n-1, 0)
