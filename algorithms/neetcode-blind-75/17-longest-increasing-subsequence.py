"""
TC: O(n^2)
SC: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1] * n

        for j in range(1, n, 1):
            for i in range(j):
                if nums[i] < nums[j]:
                    arr[j] = max(arr[i]+1, arr[j])

        return max(arr)

"""

"""
Optimized Binary search solution (Trick)
TC: O(n log n)
SC: O(n)
"""
class Solution:

    def binary_search_lower_bound(self, arr, target):
        start, end = 0, len(arr) - 1

        while start <= end:
            mid = (start + end) // 2

            if arr[mid] < target:
                start = mid+1
            else:
                end = mid - 1

        return start


    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [nums[0]]


        for i in range(1, n, 1):
            num = nums[i]
            if arr[-1] < num:
                arr.append(num)
            else:
                index = self.binary_search_lower_bound(arr, num)
                arr[index] = num

        return len(arr)
