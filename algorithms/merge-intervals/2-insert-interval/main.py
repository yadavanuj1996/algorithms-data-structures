
"""
Insert Interval

Statement
Given a sorted list of nonoverlapping intervals and a new interval, your task is to insert the new interval 
into the correct position while ensuring that the resulting list of intervals remains sorted and nonoverlapping.
 Each interval is a pair of nonnegative numbers, the first being the start time and the second being the end
time of the interval.

Constraints:
- 0 <= existing_intervals.length ≤ 10^4
- existing_intervals[i].length, new_interval.length == 2
- 0 ≤ start time, end time ≤ 10^4
- The first number should always be less than the second number in each interval.
- The list of intervals is sorted in ascending order based on the first element in every interval.

Test Case:
Input:
Existing Intervals = [ [1,3], [5, 7], [8, 9], [10, 13] ]
New Intervals = [2, 6]
    
Output:
[ [1,7], [8,9], [10,13] ]
"""



from interval import *

"""
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
def insert_interval(existing_intervals, new_interval):
    existing_intervals.append(new_interval)
    intervals = existing_intervals
    intervals.sort(key=lambda x: x.start)
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
