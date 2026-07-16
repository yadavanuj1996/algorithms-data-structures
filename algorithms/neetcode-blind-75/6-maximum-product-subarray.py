"""
TC: O(n)
SC: O(1)

Optimized approach (single pass, prefix & suffix together)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        prefix = 1
        suffix = 1
        n = len(nums)
        res = float("-inf")

        j = n-1
        for i in range(0, n):
            j = n-1-i

            prefix *= nums[i]
            suffix *= nums[j]

            res = max(res, prefix, suffix)

            if nums[i] == 0:
                prefix = 1

            if nums[j] == 0:
                suffix = 1


        return res
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        prefix = 1
        suffix = 1
        no_of_neg = 0
        n = len(nums)
        res = float("-inf")

        for i in range(0, n):
            prefix *= nums[i]
            res = max(res, prefix)

            if nums[i] == 0:
                prefix = 1


        for i in range(n-1, -1, -1):
            suffix *= nums[i]
            res = max(res, suffix)

            if nums[i] == 0:
                suffix = 1

        return res
