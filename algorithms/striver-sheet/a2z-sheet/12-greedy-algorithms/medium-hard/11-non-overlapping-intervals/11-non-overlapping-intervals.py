"""
Non-overlapping Intervals

Problem Link:
https://leetcode.com/problems/non-overlapping-intervals/

Statement
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of 
intervals you need to remove to make the rest of the intervals non-overlapping.

Constraints:
- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= start[i] < end[i] <= 5 * 10^4


Test Case:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

"""

"""
Time complexity: O(N log N) + O(N)
Space complexity: O(1)
"""
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
        
