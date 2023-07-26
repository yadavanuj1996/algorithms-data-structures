
"""
Merge Intervals

Statement
We are given an array of closed intervals, intervals, where each interval has a start time and an end time.
The input array is sorted with respect to the start times of each interval. For example, 
intervals = [ [1,4], [3,6], [7,9] ] is sorted in terms of start times 1, 3 and 7.

Your task is to merge the overlapping intervals and return a new output array consisting of only the
non-overlapping intervals.


Constraints:
- 1 ≤ intervals.length ≤ 10^4
- intervals[i].length = 2
- 0 ≤ start time ≤ end time ≤ 10^4

Test Case:
Input:
intervals = [[1, 5], [3, 7] ,[4, 6], [6, 8]]
    
Output:
[[1,8]]
"""

from interval import *

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
def merge_intervals(intervals):
    size = len(intervals)
    result = []
    current, next = 0,1 
    start, end = 0, 1

    while next < size:
        if intervals[current].start <= intervals[next].start <= intervals[current].end:
            intervals[current].start = min(intervals[current].start, intervals[next].start)
            intervals[current].end = max(intervals[current].end, intervals[next].end)

            next += 1 
            continue
    
        result.append(intervals[current])
        current = next
        next += 1
    
    result.append(intervals[current])

    return result

def main():
    #intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [18, 20]]
    intervals = [[10, 12]]
    print(merge_intervals(intervals))

if __name__ == "__main__":
    main()


"""
Iteration 2 (This is solution for leetcode version of the problem)
# https://leetcode.com/problems/merge-intervals/
# There is an extra step of sorting the intervals as in leetcode the input intervals are not in sorted order
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

"""