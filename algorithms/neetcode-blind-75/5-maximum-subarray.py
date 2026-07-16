"""
TC: O(n)
SC: O(1)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        cur_sum = float("-inf")
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] > cur_sum + nums[i]:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]

            if cur_sum > max_sum:
                max_sum = cur_sum

            i += 1

        return max_sum
