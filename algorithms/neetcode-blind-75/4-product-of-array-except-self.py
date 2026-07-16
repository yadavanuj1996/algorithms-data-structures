"""
TC: O(N)
SC: O(1) (+ O(N) auxilary space for output)
"""
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n

        left_prod = 1
        for i in range(0, n):
            output[i] = left_prod
            left_prod *= nums[i]

        right_prod = 1
        for i in range(n-1, -1, -1):
            output[i] *= right_prod
            right_prod *= nums[i]

        return output
