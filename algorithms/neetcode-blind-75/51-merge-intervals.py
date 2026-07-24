"""
TC: O(n log n)
SC: O(n)
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        size = len(intervals)
        result = []

        current, next = 0,1
        start, end = 0, 1

        while next < size:
            if intervals[current][start] <= intervals[next][start] <= intervals[current][end]:
                intervals[current][start] = min(intervals[current][start], intervals[next][start])
                intervals[current][end] = max(intervals[current][end], intervals[next][end])

                next += 1
                continue

            result.append(intervals[current])
            current = next
            next += 1

        result.append(intervals[current])

        return result
