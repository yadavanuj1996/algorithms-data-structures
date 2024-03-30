"""
Insert Interval

Problem Link:
https://leetcode.com/problems/insert-interval/

Statement
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent
the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are 
also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and 
intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^5
- intervals is sorted by start[i] in ascending order.
- newInterval.length == 2
- 0 <= start <= end <= 10^5


Test Case:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

"""

"""
Time complexity: O(N log N) + O(N)
Space complexity: O(N)
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            intervals.append(newInterval)
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
