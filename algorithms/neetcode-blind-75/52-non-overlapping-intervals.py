"""
TC: O(n log n)
SC: O(1)
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals on the basis of end time of interval
        intervals.sort(key=lambda x: x[1])
        res,ind = 0, 0

        while ind < len(intervals)-1:
            cur_interval_end = intervals[ind][1]
            next_interval_start = intervals[ind+1][0]
            # pop next interval if the next interval overlaps with cur one
            if next_interval_start < cur_interval_end:
                intervals.pop(ind+1)
                res += 1
                continue

            ind += 1

        return res
