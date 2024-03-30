"""
Merge Intervals

Problem Link:
https://leetcode.com/problems/merge-intervals/

Statement
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4


Test Case:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

"""

"""
Time complexity: O(N log N) + O(N)
Space complexity: O(N)
"""
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