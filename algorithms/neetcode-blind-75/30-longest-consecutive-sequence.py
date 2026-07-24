"""
TC: O(n)
SC: O(n)
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        res = 1
        nums_set = set()

        for item in nums:
            nums_set.add(item)

        for no in nums_set:
            if no-1 not in nums_set:
                count = 1
                while no+1 in nums_set:
                    count += 1
                    no += 1

                res = max(res, count)

        return res
