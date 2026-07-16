"""
TC: O(n)
SC: O(n) memo + O(n) recursion stack

Circular street => either rob houses [0..n-2] (exclude last) or [1..n-1] (exclude first),
then take the max of the two linear House Robber runs.
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
