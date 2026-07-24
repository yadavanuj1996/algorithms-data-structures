"""
TC: O(n log n)
SC: O(n)
"""
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}

        for num in nums:
            data[num] = data[num] + 1 if data.get(num) else 1

        res = []

        for key, val in (sorted(data.items(), key= lambda item: -item[1])):
            if k > 0:
                res.append(key)
                k -= 1

        return res
