"""
TC: O(log n)
SC: O(1)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search solution
        n = len(nums)
        start, end = 0, n-1
        res = float("inf")

        while start <= end:
            mid = (start + end) // 2

            is_left_sorted = True if nums[start] <= nums[mid] else False

            if is_left_sorted:
                res = min(res, nums[start])
                start = mid + 1
            else:
                res = min(res, nums[mid])
                end = mid - 1

        return res
