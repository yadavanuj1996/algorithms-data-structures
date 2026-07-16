"""
TC: O(log n)
SC: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1

        while low <= high:
            mid = (low+high) // 2

            if nums[mid] == target:
                return mid

            is_left_half_sorted = nums[low] <= nums[mid]

            if is_left_half_sorted:
                if nums[low] <= target and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            # is right half sorted
            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1

        return -1
